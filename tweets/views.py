from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tweet, Follow
from .forms import TweetForm
from django.contrib.auth import logout
from tweets.models import Usuario
from .forms import FotoPerfilForm
from django.contrib.auth.decorators import login_required
import feedparser

@login_required
def home(request):
    if request.user.is_authenticated:
        following = request.user.following.values_list('following_id', flat=True)
        tweets = Tweet.objects.filter(user_id__in=following).order_by('-created_at')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/home.html', {'tweets': tweets})

@login_required
def tweet_detail(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    return render(request, 'tweets/tweet_detail.html', {'tweet': tweet})

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(user=user).order_by('-created_at')
    is_following = Follow.objects.filter(user=request.user, following=user).exists()
    followers_count = user.followers.count()
    following_count = user.following.count()

    usuario = Usuario.objects.filter(nome=user.username).first()
    return render(request, 'tweets/user_profile.html', {
        'profile_user': user,
        'usuario': usuario,   
        'tweets': tweets,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    })

@login_required
def feed(request):
    user = request.user
    tweets = Tweet.objects.all().order_by('-created_at')
    noticias = get_noticias()
    my_tweets = Tweet.objects.filter(user=user)
    tweets = tweets | my_tweets
    tweets = tweets.order_by('-created_at')

    # Montar um dicionário {username: Usuario}
    autores = {u.nome: u for u in Usuario.objects.all()}
    # Pega o Usuario do usuário logado
    usuario = Usuario.objects.filter(nome=user.username).first()

    return render(request, 'tweets/feed.html', {
        'tweets': tweets,
        'usuario': usuario,
        'autores': autores,
        'noticias': noticias,
    })

@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST['content']
        Tweet.objects.create(user=request.user, content=content)
        return redirect('feed')
    return render(request, 'tweets/create_tweet.html')

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    follow_instance, created = Follow.objects.get_or_create(user=request.user, following=user_to_follow)
    if not created:
        follow_instance.delete()
    return redirect('user_profile', username=username)

def user_logout(request):
    logout(request)
    return redirect('feed')

@login_required
def user_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'tweets/user_profile.html', {'profile_user': user})

@login_required
def follow_user_by_username(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    follow_instance, created = Follow.objects.get_or_create(user=request.user, following=user_to_follow)
    if not created:
        follow_instance.delete()
    return redirect('user_profile', username=username)

@login_required
def followers_list(request, username):
    user = get_object_or_404(User, username=username)
    followers = user.followers.all()
    return render(request, 'tweets/followers_list.html', {'profile_user': user, 'followers': followers})


@login_required
def trocar_foto(request):
    usuario = Usuario.objects.filter(nome=request.user.username).first()
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = FotoPerfilForm(instance=usuario)
    return render(request, 'tweets/trocar_foto.html', {'form': form})


def get_noticias():
    # Você pode mudar o feed para outro portal se quiser
    feed_url = "https://g1.globo.com/rss/g1/"
    feed = feedparser.parse(feed_url)
    noticias = []
    for entry in feed.entries[:5]:  # pega as 5 primeiras
        noticias.append({
            'titulo': entry.title,
            'link': entry.link
        })
    return noticias
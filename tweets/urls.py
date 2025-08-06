from django.urls import path
from .views import feed, follow_user_by_username, user_profile, create_tweet, user_logout, followers_list, trocar_foto

urlpatterns = [
    path('', feed, name='feed'),  
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('follow/<str:username>/', follow_user_by_username, name='follow_user_by_username'),
    path('create-tweet/', create_tweet, name='create_tweet'),
    path('logout/', user_logout, name='logout'),
    path('followers/<str:username>/', followers_list, name='followers_list'),
    path('trocar-foto/', trocar_foto, name='trocar_foto'),
]

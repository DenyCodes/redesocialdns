from django.db import models
from django.contrib.auth.models import User
from django import forms

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} follows {self.following}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(
        upload_to='usuarios/', 
        default='usuarios/Denis.jpg'
    )

    def __str__(self):
        return self.nome
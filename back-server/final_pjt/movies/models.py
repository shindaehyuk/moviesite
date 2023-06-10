# Create your models here.
from django.db import models
from django.conf import settings


# Create your models here.

#장르 모델 
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#무비모델
class Movie(models.Model):
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rated_movies')
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=255, null=True)

#영화에 대한 댓글
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=50,)
    star = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#커뮤니티 아티클
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

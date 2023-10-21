from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)
    Release_year = models.PositiveIntegerField(null=True,blank=True)
    Rating = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True)
    Actor = models.CharField(max_length=200)
    Pop_now = models.BooleanField(default=False)
    image_url = models.CharField(max_length=5000)
    Language = models.CharField(max_length=200,default='')
    Genre = models.CharField(max_length=200,default='')
    Type = models.CharField(max_length=200,default='')
    Seriess = models.BooleanField(default=False)
    video = EmbedVideoField(
        max_length=200,
        null=True,
        blank=True
    )


class Series(models.Model):
    Name = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    Description = models.TextField(max_length=2000)
    Year = models.PositiveIntegerField(null=True,blank=True)
    Actors = models.CharField(max_length=200)
    pop_now = models.BooleanField(default=False)
    image_url = models.CharField(max_length=5000)
    Genre = models.CharField(max_length=200)
    Rating = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True)

class watchlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movies)
    series = models.ManyToManyField(Series)
    
class moviestowatch(models.Model):
    movie1 = models.ForeignKey(Movies,on_delete=models.CASCADE)
    series1 = models.ForeignKey(Series,on_delete=models.CASCADE)
    movielist = models.ForeignKey(watchlist,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s Watchlist: {self.movie.title}"
    


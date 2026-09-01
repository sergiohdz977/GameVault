from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    platform = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    rating = models.IntegerField(choices=[(i,i) for i in range(1, 6)])
    comment = models.TextField(max_length= 300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)



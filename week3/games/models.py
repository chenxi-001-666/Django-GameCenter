from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tags(models.Model):
    label = models.CharField(max_length=20)


class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    label_tag = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, default="default-slug") # 建议加 unique
    cover_image = models.ImageField(upload_to='game_covers/', null=True, blank=True)
    description = models.TextField(default="No description.")

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"


class GameReview:
    model = Review
    template_name = 'games/review_list.html'
    context_object_name = 'game_reviews'
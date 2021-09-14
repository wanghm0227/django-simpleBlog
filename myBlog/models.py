from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=CASCADE, null=False)
    tag = models.CharField(max_length=255)
    category = models.CharField(max_length=50, default="coding")
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    post_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="like_list")

    class Meta:
        ordering = ['-post_time']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title} | {self.author}'

    def get_absolute_url(self):
        return reverse('article_detail', args=(str(self.pk),))


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="comments")
    body = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.utils import timezone


class Question(models.Model):
    username=models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

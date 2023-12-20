from django.db import models

# Create your models here.
from django.db import models

class Conversation(models.Model):
    user_input = models.CharField(max_length=255)
    chatgpt_response = models.TextField()
from django.db import models

# models.py
from django.db import models

class GeneratedText(models.Model):
    user_input = models.TextField()
    generated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_input} - {self.created_at}'

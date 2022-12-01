from django.db import models

# Create your models here.

class Quession(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    quession = models.TextField()
    body_answer = models.TextField(default='')
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['publish']

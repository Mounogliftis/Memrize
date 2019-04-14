from django.db import models

class Poems(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    text = models.TextField(default="Dimitri")

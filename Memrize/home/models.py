from django.db import models

class Poem(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    text = models.TextField(default="Dimitri")

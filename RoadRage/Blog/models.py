from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    creation_date = models.TextField()
    author = models.TextField()


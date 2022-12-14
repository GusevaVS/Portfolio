from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

from django.db import models


class Project(models.Model):   
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.CharField(max_length=20)
    technology = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title
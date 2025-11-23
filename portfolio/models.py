from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField("date started")
    end_date = models.DateTimeField("date completed")
    git_url = models.URLField(default="https://github.com/NewtC1/django-learning")
    last_git_commit = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class User():
  username=models.CharField(max_length=50)
  def __str__(self):
    return self.username


class Event():
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=200)
  date=models.DateField()
  user_id=models.ForeignKey(User, ondelete=models.CASCADE, related_name='events')

  def __str__(self):
    return self.title
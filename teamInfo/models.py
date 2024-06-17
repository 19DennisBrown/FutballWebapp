from django.db import models

# Create your models here.



class Team(models.Model):
  title = models.CharField(max_length=100)
  # titles_won = models.IntegerField()
  year_founded = models.IntegerField()
  # name_initials = models.CharField(max_length=4)

  def __str__(self):
    return self.name

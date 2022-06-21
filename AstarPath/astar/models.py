from django.db import models

class adjancedmap(models.Model):
  firstCity = models.CharField(max_length=255)
  secondCity = models.CharField(max_length=255)
  cost= models.FloatField()
class heuristic(models.Model):
  city=models.CharField(max_length=255)
  Hval=models.FloatField()

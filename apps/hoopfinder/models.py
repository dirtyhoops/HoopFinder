from django.db import models

# Create your models here.
class Courts(models.Model):
    name = models.CharField(max_length=255)
    court_picture = models.FileField()
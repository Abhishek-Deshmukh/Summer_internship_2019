from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000)
    context = models.CharField(max_length=100000)
    grant_support = models.CharFiels(max_length=30)
    images = models.ImageField(upload_to='images/res/', blank=True)

def __str__(self):
    return self.name

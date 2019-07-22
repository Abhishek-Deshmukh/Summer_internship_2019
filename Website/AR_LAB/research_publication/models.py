from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=1000)
    context = models.CharField(max_length=100000)
    grant_support = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/res/', blank=True)


class Publication(models.Model):
    content = models.CharField(max_length=1000)
    publication = models.CharField(max_length=100)
    year = models.IntegerField()
    page_no = models.CharField(max_length=20)

def __str__(self):
    return self.name

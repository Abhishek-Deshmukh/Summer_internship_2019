from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, blank=True)
    institute = models.CharField(max_length=100)
    designation = models.CharField(max_length=20,choices=(
        ('prof', 'Professor'),
        ('masters', 'Masters Student'),
        ('phd', 'Research Students:Ph.D'),
        ('des', 'Dissertation Student'),
        ('alumni', 'Alumni'),
        ))
    image = models.ImageField(upload_to='images/', blank=True)

def __str__(self):
    return self.name

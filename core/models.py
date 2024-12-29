from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, blank=True, null=True) 

    def __str__(self):
        return self.name or "Unnamed Person"

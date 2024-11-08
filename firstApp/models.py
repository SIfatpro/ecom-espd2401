from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
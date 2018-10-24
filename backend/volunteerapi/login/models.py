from django.db import models

# Create your models here.

class LoginUser(models.Model):
    name = models.CharField(max_length=200)
    passw = models.CharField(max_length=200)

    def __str__(self):
        return self.name
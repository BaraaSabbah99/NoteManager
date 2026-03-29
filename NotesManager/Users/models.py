from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    role = models.CharField(max_length=20,default='user') 


    def __str__(self):
        return self.username



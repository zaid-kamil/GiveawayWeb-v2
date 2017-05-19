from django.db import models

# Create your models here.
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=55,)
    email=models.EmailField()
    location=models.CharField(max_length=20)
    msg = models.TextField(max_length=500 )


    def publish(self):
        self.save()

    def __str__(self):
        return self.email

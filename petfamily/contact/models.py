from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    from_email = models.EmailField()
    message = models.CharField(max_length=200)

def __str__(self):
    return self.name

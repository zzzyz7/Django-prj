from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.contrib.auth.models import User 

PET_CHOICES = (
    ('Cat', 'CAT'),
    ('Dog', 'DOG'),
)

AGE_CHOICES = (
    ('Young', 'YOUNG'),
    ('Old', 'OLD'),
)

SEX_CHOICES = (
    ('Male', 'MALE'),
    ('Female','FEMALE'),
)


class Pet(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=20)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, blank=True)
    age = models.FloatField(max_length=5)
    image = models.CharField(max_length=400)
    description = models.TextField(max_length=300)
    friendly = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True)
    sheltered_time = models.DateField(default=datetime.date.today, blank=True)
    
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        if self is None:
            return f'None'
        else:
            return self.name
    
    def hasUserFavourite(pet, userID):
        return pet.favourite.filter(id=userID).exists()

from django.db import models
from .validators import file_size
# Create your models here.
class Upload(models.Model):
    PetName = models.CharField(max_length=100)
    YourName = models.CharField(max_length=100)
    ShortDescription = models.CharField(max_length=200)
    Instructions = models.TextField()
    Photo = models.ImageField(upload_to='photo_recipe', blank=True, validators=[file_size])
    #Video= models.FileField(upload_to='video_recip/%y', blank=True, validators=[file_size])
    def __str__(self):
        return self.PetName
    class Meta:
        db_table = "myapp_image"

# class User(models.Model):

#     # gender = (
#     #     ('male', "male"),
#     #     ('female', "female"),
#     # )

#     username = models.CharField(max_length=128, unique=True)
#     password = models.CharField(max_length=256)
#     email_address = models.EmailField(unique=True)
#     # sex = models.CharField(max_length=32, choices=gender, default="male")
#     # c_time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name

    # class Meta:
    #     ordering = ["-c_time"]
    #     verbose_name = "user"
    #     verbose_name_plural = "user"
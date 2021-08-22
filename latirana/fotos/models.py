from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.tags
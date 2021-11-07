from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField



# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=300)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('home')

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    
    def save_location(self):
        self.save()

    
    def update_location(self, name):
        self.name = name
        self.save()

    
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name    






class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,default='dan')
  category = models.CharField(max_length=200,default='supercar')
  images =  CloudinaryField( 'image', null=True, )
  body = models.TextField()
  location=models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


  def __str__(self):
    return self.title 

  def get_absolute_url(self):
    return reverse('home')
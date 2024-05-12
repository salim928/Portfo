from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()


    def __str__(self):
        return self.name
    
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    authname = models.CharField(max_length=30)
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


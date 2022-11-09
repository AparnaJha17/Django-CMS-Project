from multiprocessing import AuthenticationError
from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="name")
    details = models.CharField(max_length=200,default="DETAILS")
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Banner(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    title = models.CharField(max_length=200, default='title')
    description = models.CharField(max_length=200, default='title')

    def __str__(self) -> str:
        return self.name


class Social(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    link = models.CharField(max_length=200, default='#')
    

    def __str__(self) -> str:
        return self.name[:10]

class Story(models.Model):
    message = models.TextField(default="#")
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, default="#")
    place = models.CharField(max_length=200, default="#")

    def __str__(self) -> str:
        return self.name 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class News(models.Model):
    title = models.CharField(max_length=200, default="#")
    slug = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title 
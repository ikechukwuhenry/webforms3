from django.db import models

# Create your models here.
class Users(models.Model):
    """docstring for ."""
    #def __init__(self, arg):
        #super(, self).__init__()
        #self.arg = arg
    #email = models.EmailField(unique=True,blank=False)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=20, blank=False, default="1234")

class Article(models.Model):
    """docstring for ."""
    pub_date = models.DateField()
    headline = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    reporter = models.CharField(max_length=250)

class Musician(models.Model):
    """docstring for ."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

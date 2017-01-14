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

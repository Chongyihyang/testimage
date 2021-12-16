from django.db import models

class Post(models.Model):
    Image=models.ImageField(upload_to="media",null=True,blank=True)
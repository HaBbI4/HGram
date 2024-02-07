from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d/", default='avatars/default.png', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    

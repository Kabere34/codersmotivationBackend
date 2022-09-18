from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  # Boolean fiels to select the type of account
   is_admin = models.BooleanField(default=False)
   is_staff= models.BooleanField(default=False)


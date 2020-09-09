from django.db import models

# Create your models here.
from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    dpartment = models.CharField(max_length=255 ,default="")
    def __str__(self):
        return "@{}".format(self.username)

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(default=False, null=False, blank=False)


class User(AbstractUser):
    phone = models.TextField(max_length='14', null=True, blank=True)

# Abstract: Course -> db
#           BaseModel -> -

# One-to-One: User -> db (Fname, Lname, ...)
#           Student -> db ({FK -> User}, Photo, Degree, ...)

# Proxy: User (Proxy)   -> db (Fname, Lname, ...)
#        Student        -> -  (functions,...)

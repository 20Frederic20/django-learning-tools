from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import DBOject
from uuid import uuid4
# Create your models here.

class User(AbstractUser, DBOject):
    uuid = models.UUIDField(default=uuid4)

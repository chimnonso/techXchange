from django.db import models
from django.contrib.auth.models import AbstractUser
from hashlib import md5
# Create your models here.


class User(AbstractUser):
    def avatar(self):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={128}'
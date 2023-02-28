from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'User: {self.username}, email: {self.email}, first_name: {self.first_name}, last_name: {self.last_name}, profile_picture: {self.profile_picture}'

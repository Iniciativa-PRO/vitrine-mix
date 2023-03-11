from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', blank=True, null=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'User: {self.username}, email: {self.email}, first_name: {self.first_name}, last_name: {self.last_name}, profile_picture: {self.profile_picture}'


class StoreFront(models.Model):
    objects = models.Manager()
    background = models.ImageField(upload_to=upload_to, blank=True, null=True)
    name = models.CharField(max_length=30, blank=False)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    theme = models.CharField(max_length=10, blank=False)
    description = models.TextField(max_length=100, blank=False)
    is_schedulable = models.BooleanField(default=True)
    address_text = models.CharField(max_length=50, blank=False)
    address_CEP = models.CharField(max_length=8, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    facebook = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    youtube = models.CharField(max_length=30, blank=True)
    creator = models.ForeignKey(
        UserAccount,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'background: {self.background}, ' \
               f'name: {self.name}, ' \
               f'logo: {self.logo}, ' \
               f'theme: {self.theme}, ' \
               f'description: {self.description}, ' \
               f'is_schedulable: {self.is_schedulable}, ' \
               f'address_text: {self.address_text}, ' \
               f'address_CEP: {self.address_CEP}, ' \
               f'phone: {self.phone}, ' \
               f'opening_time: {self.opening_time}, ' \
               f'closing_time: {self.closing_time}, ' \
               f'facebook: {self.facebook}, ' \
               f'instagram: {self.instagram}, ' \
               f'youtube: {self.youtube} '


class Services(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_time = models.DurationField()
    store = models.ForeignKey(
        StoreFront,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'name: {self.name}, ' \
               f'price: {self.price}, ' \
               f'duration_time: {self.duration_time}, ' \
               f'store: {self.store} '

from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'User: {self.username}, email: {self.email}, first_name: {self.first_name}, last_name: {self.last_name}, profile_picture: {self.profile_picture}'


class Services:
    pass


class StoreFront(models.Model):
    background = models.ImageField(upload_to=upload_path_handler, blank=True)
    name = models.TextField(max_length=30, blank=False)
    logo = models.ImageField(upload_to=upload_path_handler, blank=True)
    theme = models.TextField(max_length=10, blank=False)
    description = models.TextField(max_length=100, blank=False)
    is_schedulable = models.BooleanField(default=True)
    address_text = models.TextField(max_length=100, blank=False)
    address_CEP = models.TextField(max_length=8, blank=False)
    phone = models.TextField(max_length=11, blank=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    facebook = models.TextField(max_length=30, blank=True)
    instagram = models.TextField(max_length=30, blank=True)
    youtube = models.TextField(max_length=30, blank=True)
    owner = models.ForeignKey(
        UserAccount,
        on_delete=models.DO_NOTHING()
    )

    def __str__(self):
        return  f'background: {self.background}, ' \
                f'name: {self.name}, ' \
                f'logo: {self.logo}, ' \
                f'theme: {self.theme}, ' \
                f'description: {self.description}, ' \
                f'is_schedulable: {self.is_schedulable}, ' \
                f'services: {self.services}, ' \
                f'address_text: {self.address_text}, ' \
                f'address_CEP: {self.address_CEP}, ' \
                f'phone: {self.phone}, ' \
                f'opening_time: {self.opening_time}, ' \
                f'closing_time: {self.closing_time}, ' \
                f'facebook: {self.facebook}, ' \
                f'instagram: {self.instagram}, ' \
                f'youtube: {self.youtube} '


class Services(models.Model):
    name = models.TextField(max_length=100, blank=False)
    price = models.DecimalField()
    duration_time = models.TimeField()
    store_id = models.ForeignKey(
        StoreFront,
        on_delete=models.DO_NOTHING(),
    )

    def __str__(self):
        return f'name: {self.name}, ' \
                f'price: {self.price}, ' \
                f'duration_time: {self.duration_time}, ' \
                f'store_id: {self.store_id} '
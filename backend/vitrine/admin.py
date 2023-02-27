from django.contrib import admin

# Register your models here.

from vitrine.models import UserAccount


# Define a new User admin


admin.site.register(UserAccount)

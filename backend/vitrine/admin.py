from django.contrib import admin

# Register your models here.

from .models import UserAccount, StoreFront, Services


class List_StoreFronts(admin.ModelAdmin):
    list_display = ("id", "name", "creator")
    search_fields = ("name", )
    list_filter = ("creator", )


class List_Services(admin.ModelAdmin):
    list_display = ("id", "name", "store")
    search_fields = ("name", )
    list_filter = ("store", )


admin.site.register(UserAccount, )
admin.site.register(StoreFront, List_StoreFronts)
admin.site.register(Services, List_Services)

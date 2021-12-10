from django.contrib import admin

from .models import DriverModel


@admin.register(DriverModel)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

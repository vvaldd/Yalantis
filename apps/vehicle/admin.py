from django.contrib import admin

from .models import VehicleModel


@admin.register(VehicleModel)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'plate_number')

from django.db import models

from ..driver.models import DriverModel


class VehicleModel(models.Model):
    """
    create model vehicle
    """
    class Meta:
        db_table = 'vehicles'
        verbose_name = 'vehicle'

    driver_id = models.ForeignKey(DriverModel, on_delete=models.PROTECT, null=True)
    make: str = models.CharField(max_length=20)
    model: str = models.CharField(max_length=20)
    plate_number: str = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

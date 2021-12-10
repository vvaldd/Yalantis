from django.db import models


class DriverModel(models.Model):
    """
    create model driver model
    """

    class Meta:
        db_table = 'drivers'
        verbose_name = 'driver'

    first_name: str = models.CharField(max_length=20)
    last_name: str = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

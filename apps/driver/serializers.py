from rest_framework import serializers

from .models import DriverModel


class DriverSerializer(serializers.ModelSerializer):
    """
    serializers for driver
    """
    class Meta:
        model = DriverModel
        fields = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')

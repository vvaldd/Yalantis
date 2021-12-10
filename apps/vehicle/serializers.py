import re
from rest_framework import serializers

from .models import VehicleModel


class VehicleSerializer(serializers.ModelSerializer):
    """
    serializers for vehicle
    """
    class Meta:
        model = VehicleModel
        fields = ('id', 'make', 'model', 'plate_number', 'driver_id', 'created_at', 'updated_at')
        extra_kwargs = {
            'driver_id': {'required': False}
        }
    """
    create vehicle and format field plate_number
    """
    def create(self, validated_data):
        number = validated_data.pop('plate_number')
        match_pattern = r'^(\w{2})(\d{4})(\w{2})'
        replace_pattern = r'\1 \2 \3'
        number_format = re.sub(match_pattern, replace_pattern, number).upper()
        vehicle = VehicleModel.objects.create(plate_number=number_format, **validated_data)
        return vehicle


class SetDriverSerializer(VehicleSerializer):
    """
    install the driver in vehicle
    """
    class Meta:
        model = VehicleModel
        fields = ('driver_id',)


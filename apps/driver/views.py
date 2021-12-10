from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .driver_filters import DriverFilter
from .models import DriverModel
from .serializers import DriverSerializer


class DriverListCreate(ListCreateAPIView):
    """
    create/views vehicle and filtering by field created_at
    """
    serializer_class = DriverSerializer
    queryset = DriverModel.objects.all()
    filterset_class = DriverFilter
    filterset_fields = ['created_at']


class DriverRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    put/patch/delete vehicle
    """
    serializer_class = DriverSerializer
    queryset = DriverModel.objects.all()

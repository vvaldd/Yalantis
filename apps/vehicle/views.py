from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from .models import VehicleModel
from .serializers import VehicleSerializer, SetDriverSerializer


class VehicleListCreate(ListCreateAPIView):
    """
    create/views vehicle
    """
    serializer_class = VehicleSerializer
    """
    filter query_params - with_drivers yes or no
    """
    def get_queryset(self):
        queryset = VehicleModel.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == 'no':
            queryset = queryset.filter(driver_id__isnull=True)
        elif with_drivers == 'yes':
            queryset = queryset.filter(driver_id__isnull=False)
        return queryset


class VehicleRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    put/patch/delete vehicle
    """
    serializer_class = VehicleSerializer
    queryset = VehicleModel.objects.all()


class SetDriverMode(UpdateAPIView):
    """
    install the driver in vehicle
    """
    serializer_class = SetDriverSerializer
    queryset = VehicleModel.objects.only('driver_id')

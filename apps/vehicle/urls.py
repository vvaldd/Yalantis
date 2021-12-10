from django.urls import path

from .views import VehicleListCreate, VehicleRetrieveUpdateDestroy, SetDriverMode

urlpatterns = [
    path('vehicle/', VehicleListCreate.as_view(), name='vehicle_create_list'),
    path('vehicle/<int:pk>/', VehicleRetrieveUpdateDestroy.as_view(), name='vehicle_retrieve_update_destroy'),
    path('set_driver/<int:pk>/', SetDriverMode.as_view(), name='set_driver')
    ]

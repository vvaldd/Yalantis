from django.urls import path

from .views import DriverListCreate, DriverRetrieveUpdateDestroy

urlpatterns = [
    path('driver/', DriverListCreate.as_view(), name='driver_create_list'),
    path('driver/<int:pk>/', DriverRetrieveUpdateDestroy.as_view(), name='driver_retrieve_update_destroy'),
    ]

from django.urls import path, include

urlpatterns = [
    path('drivers/', include('apps.driver.urls')),
    path('vehicles/', include('apps.vehicle.urls')),
    ]

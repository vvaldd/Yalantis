from django_filters import DateFilter, FilterSet

from .models import DriverModel


class DriverFilter(FilterSet):
    """
    create filter by field created_at
    """
    create_at = DateFilter()

    class Meta:
        model = DriverModel
        fields = {
            'created_at': ('lte', 'gte')
        }

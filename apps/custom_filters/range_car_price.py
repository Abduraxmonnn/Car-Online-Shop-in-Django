from django_filters import FilterSet, RangeFilter

from apps.car.models import Car

class CarFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Car
        fields = [
            'model__name',
            'model__brand__name',
            'color',
            'transmission__type',
            'year',
            'body__name',
            'engine',
            'max_speed',
        ]

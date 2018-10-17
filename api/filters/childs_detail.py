

import django_filters

from ..models import ChildsDetail


class ChildsDetailFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = ChildsDetail
        fields = {
            'id': ['exact'],
            'child__document': ['exact', 'icontains'],
            'child__name': ['exact', 'icontains'],
            'height': ['exact', 'icontains'],
            'weight': ['exact','icontains'],
        }
        ordering_fields = ('id',  'child', 'height', 'weight',)
        

class ChildsDetailFullDataFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = ChildsDetail
        fields = {
            'id': ['exact'],
            'child': ['exact'],
            'child__document': ['exact', 'icontains'],
            'child__name': ['exact', 'icontains'],
            'height': ['exact', 'icontains'],
            'weight': ['exact','icontains'],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_by__username': ['exact', 'icontains'],
            'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'updated_by__username': ['exact', 'icontains'],
        }
        ordering_fields = ('id', 'child', 'height', 'weight',
            'created_by', 'created_at', 'updated_by', 'updated_at')
                
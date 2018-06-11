

import django_filters

from ..models import Childs


class ChildsFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = Childs
        fields = {
            'id': ['exact'],
            'name':['exact', 'icontains'],
            'document': ['exact', 'icontains'],
            'gender': ['exact'],
            'date_born': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        }
        ordering_fields = ('id', 'document', 'name', 'gender', 'date_born')
        

class ChildsFullDataFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = Childs
        fields = {
            'id': ['exact'],
            'name':['exact', 'icontains'],
            'document': ['exact', 'icontains'],
            'gender': ['exact'],
            'date_born': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_by__username': ['exact', 'icontains'],
            'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'updated_by__username': ['exact', 'icontains'],
        }
        ordering_fields = ('id', 'document', 'name', 'gender', 'date_born', 'created_by',
                'created_at', 'updated_by', 'updated_at')
                
import django_filters

from ..models import ParentsChilds


class ParentsChildsFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = ParentsChilds
        fields = {
            'id': ['exact'],
            'parent':['exact',],
            'child':['exact',],
            'relationship':['exact',],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],             
            'created_by': ['exact'],
        }
        ordering_fields = ('id', 'parent', 'child', 'relationship')
        

class ParentsChildsFullDataFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = ParentsChilds
        fields = {
            'id': ['exact'],
            'parent':['exact',],
            'child':['exact',],
            'relationship':['exact',],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_by__username': ['exact', 'icontains'],
            'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'updated_by__username': ['exact', 'icontains'],
        }
        ordering_fields = ('id', 'parent', 'child', 'relationship', 'created_at', 'created_by', 'updated_at', 'updated_by')
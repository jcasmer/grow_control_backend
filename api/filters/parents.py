

import django_filters

from ..models import Parents


class ParentsFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = Parents
        fields = {
            'id': ['exact'],
            'name':['exact', 'icontains'],
            'document_type': ['exact'],
            'document': ['exact', 'icontains'],
            'age': ['exact', 'icontains'],
            'gender': ['exact'],
            'relationship': ['exact'],
            'phone_number': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'social_stratum': ['exact',],
            'phone_number': ['exact', 'icontains'],
            'height': ['exact', 'icontains'],
            'weight': ['exact', 'icontains'],
            'is_active': ['exact'],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_by__username': ['exact', 'icontains'],
            'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'updated_by__username': ['exact', 'icontains'],
        }
        ordering_fields = ('id', 'document_type', 'document', 'name', 'age', 'gender', 'relationship',
                'phone_number', 'email', 'social_stratum', 'height', 'weight', 'is_active', 'created_by',
                'created_at', 'updated_by', 'updated_at')
        

class ParentsFullDataFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = Parents
        fields = {
            'id': ['exact'],
            'name':['exact', 'icontains'],
            'document_type': ['exact'],
            'document': ['exact', 'icontains'],
            'age': ['exact', 'icontains'],
            'gender': ['exact'],
            'relationship': ['exact'],
            'phone_number': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'social_stratum': ['exact',],
            'phone_number': ['exact', 'icontains'],
            'height': ['exact', 'icontains'],
            'weight': ['exact', 'icontains'],
            'is_active': ['exact'],
            'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'created_by__username': ['exact', 'icontains'],
            'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
            'updated_by__username': ['exact', 'icontains'],
        }
        ordering_fields = ('id', 'document_type', 'document', 'name', 'age', 'gender', 'relationship',
                'phone_number', 'email', 'social_stratum', 'height', 'weight', 'is_active', 'created_by',
                'created_at', 'updated_by', 'updated_at')
                
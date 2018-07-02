'''
'''
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import ParentsChilds
from ..serializers import ParentsChildsSerializer, ParentsChildsFullDataSerializer
from ..filters import ParentsChildsFilter, ParentsChildsFullDataFilter


class ParentsChildsViewSet(BaseViewSet):
    '''
    Parents Childs view
    FILTERS:
        'id': ['exact'],
        'description':['exact', 'icontains'],
        'type_diagnostic':['exact',],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],             
        'created_by': ['exact'],             
    '''
    permission_code = 'parentschilds'
    
    queryset = ParentsChilds.objects.all().select_related('parent', 'child', 'relationship', 'created_by','updated_by')
    serializer_class = ParentsChildsSerializer
    filter_class = ParentsChildsFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    
    def perform_destroy(self, serializer): 
        errors = {}
        parents_childs = ParentsChilds.objects.filter(id=self.kwargs['pk'])
        if parents_childs and len(parents_childs) == 1:        
            errors['error'] = 'No se puede eliminar. Debe tener mínimo un responsable'
        if errors:
            raise ValidationError(errors)
        serializer.delete()


class ParentsChildsFullDataViewSet(BaseViewSet):
    '''
    Parents Childs views full data
    FILTROS:
        'id': ['exact'],
        'description':['exact', 'icontains'],
        'type_diagnostic':['exact',],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'created_by__username': ['exact', 'icontains'],
        'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'updated_by__username': ['exact', 'icontains'],
    '''
    permission_code = 'parentschilds'
    
    queryset = ParentsChilds.objects.all().select_related('parent', 'child', 'relationship', 'created_by','updated_by')
    serializer_class = ParentsChildsFullDataSerializer
    filter_class = ParentsChildsFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
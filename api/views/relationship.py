'''
'''
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import Relationship, Parents
from ..serializers import RelationshipSerializer, RelationshipFullDataSerializer
from ..filters import RelationshipFilter, RelationshipFullDataFilter


class RelationshipViewSet(BaseViewSet):
    '''
    Type diagnostic view
    FILTERS:
        'id': ['exact'],
        'name':['exact', 'icontains'],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],             
        'created_by': ['exact'],             
    '''
    permission_code = 'relationship'
    
    queryset = Relationship.objects.all().select_related('created_by','updated_by')
    serializer_class = RelationshipSerializer
    filter_class = RelationshipFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    def perform_create(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite create
        '''        
        try:
            type_diagnostic = Relationship.objects.filter(name=self.request.data['name'], deleted=0)            
        except:
            type_diagnostic = None
        if type_diagnostic:
            raise ValidationError({'name': ['Ya se registró este parentesco.']})              
        serializer.save()


    def perform_update(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite update
        '''
        try:
            relationship = Relationship.objects.filter(name=self.request.data['name'], deleted=0).exclude(id=self.kwargs['pk'])          
        except:
            relationship = None
        if relationship:
            raise ValidationError({'name': ['Ya se registró este parentesco.']})              
        serializer.save()

    
    def perform_destroy(self, serializer): 

        errors = {}
        relationship = Parents.objects.filter(relationship=self.kwargs['pk'])
        if relationship:
            errors['error'] = 'Este parentesco ya tiene registros asociados por lo tanto no puede eliminarse.'
        if errors:
            raise ValidationError(errors)
        serializer.delete()


class RelationshipFullDataViewSet(BaseViewSet):
    '''
    Vista full data parentesco
    FILTROS:
        'id': ['exact'],
        'name':['exact', 'icontains'],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'created_by__username': ['exact', 'icontains'],
        'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'updated_by__username': ['exact', 'icontains'],
    '''
    permission_code = 'type_diagnostic'
    
    queryset = Relationship.objects.all().select_related('created_by','updated_by').order_by('name')
    serializer_class = RelationshipFullDataSerializer
    filter_class = RelationshipFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
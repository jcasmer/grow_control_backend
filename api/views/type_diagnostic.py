'''
'''

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import TypeDiagnostic, Advices
from ..serializers import TypeDiagnosticSerializer, TypeDiagnosticFullDataSerializer
from ..filters import TypeDiagnosticFilter, TypeDiagnosticFullDataFilter


class TypeDiagnosticViewSet(BaseViewSet):
    '''
    Type diagnostic view
    FILTERS:
        'id': ['exact'],
        'name':['exact', 'icontains'],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],             
        'created_by': ['exact'],             
    '''
    permission_code = 'type_diagnostic'
    
    queryset = TypeDiagnostic.objects.all().select_related('created_by','updated_by')
    serializer_class = TypeDiagnosticSerializer
    filter_class = TypeDiagnosticFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    def perform_create(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite create
        '''        
        try:
            type_diagnostic = TypeDiagnostic.objects.filter(name=self.request.data['name'], deleted=0)            
        except:
            type_diagnostic = None
        if type_diagnostic:
            raise ValidationError({'name': ['Ya se registró este diagnostico.']})              
        serializer.save()


    def perform_update(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite update
        '''
        try:
            type_diagnostic = TypeDiagnostic.objects.filter(name=self.request.data['name'], deleted=0).exclude(id=self.kwargs['pk'])          
        except:
            type_diagnostic = None
        if type_diagnostic:
            raise ValidationError({'name': ['Ya se registró este diagnostico.']})              
        serializer.save()

    
    def perform_destroy(self, serializer): 

        errors = {}
        advices = Advices.objects.filter(type_diagnostic=self.kwargs['pk'])
        if advices:
            errors['error'] = 'Este tipo de diagnostico ya tiene recomendaciones asociadas por lo tanto no puede eliminarse.'
        if errors:
            raise ValidationError(errors)
        serializer.delete()


class TypeDiagnosticFullDataViewSet(BaseViewSet):
    '''
    Vista full data zona abordaje
    FILTROS:
        'id': ['exact'],
        'name':['exact', 'icontains'],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'created_by__username': ['exact', 'icontains'],
        'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'updated_by__username': ['exact', 'icontains'],
    '''
    permission_code = 'type_diagnostic'
    
    queryset = TypeDiagnostic.objects.all().select_related('created_by','updated_by').order_by('name')
    serializer_class = TypeDiagnosticFullDataSerializer
    filter_class = TypeDiagnosticFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
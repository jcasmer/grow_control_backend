'''
'''
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import TypeDiagnostic, Advices
from ..serializers import AdvicesSerializer, AdvicesFullDataSerializer
from ..filters import AdvicesFilter, AdvicesFullDataFilter


class AdvicesViewSet(BaseViewSet):
    '''
    Type diagnostic view
    FILTERS:
        'id': ['exact'],
        'description':['exact', 'icontains'],
        'type_diagnostic':['exact',],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],             
        'created_by': ['exact'],             
    '''
    permission_code = 'advices'
    
    queryset = Advices.objects.all().select_related('created_by','updated_by')
    serializer_class = AdvicesSerializer
    filter_class = AdvicesFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    def perform_create(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite create
        '''        
        try:
            advice = Advices.objects.filter(description=self.request.data['description'], type_diagnostic=self.request.data['type_diagnostic'], deleted=0)            
        except:
            advice = None
        if advice:
            raise ValidationError({'description': ['Ya se registró esta recomendación.']})              
        serializer.save()


    def perform_update(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite update
        '''
        try:
            advice = Advices.objects.filter(description=self.request.data['description'], type_diagnostic=self.request.data['type_diagnostic'], deleted=0).exclude(id=self.kwargs['pk'])          
        except:
            advice = None
        if advice:
            raise ValidationError({'description': ['Ya se registró esta recomendación.']})              
        serializer.save()


class AdvicesFullDataViewSet(BaseViewSet):
    '''
    Vista full data zona abordaje
    FILTROS:
        'id': ['exact'],
        'description':['exact', 'icontains'],
        'type_diagnostic':['exact',],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'created_by__username': ['exact', 'icontains'],
        'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'updated_by__username': ['exact', 'icontains'],
    '''
    permission_code = 'type_diagnostic'
    
    queryset = Advices.objects.all().select_related('created_by','updated_by').order_by('description')
    serializer_class = AdvicesFullDataSerializer
    filter_class = AdvicesFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
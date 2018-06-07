'''
'''

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import Parents, ParentsChilds
from ..serializers import ParentsSerializer, ParentsFullDataSerializer
from ..filters import ParentsFilter, ParentsFullDataFilter


class ParentsViewSet(BaseViewSet):
    '''
    Parent's view
    FILTERS:
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
    '''
    permission_code = 'parents'
    
    queryset = Parents.objects.all().select_related('created_by','updated_by')
    serializer_class = ParentsSerializer
    filter_class = ParentsFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    # def perform_create(self, serializer):  # pylint: disable=arguments-differ
    #     '''
    #     Overwrite create
    #     '''        
    #     try:
    #         parents = Parents.objects.filter(name=self.request.data['document'], deleted=0)            
    #     except:
    #         parents = None
    #     if parents:
    #         raise ValidationError({'name': ['Ya se registró este documento']})              
    #     serializer.save()


    # def perform_update(self, serializer):  # pylint: disable=arguments-differ
    #     '''
    #     Overwrite update
    #     '''
    #     try:
    #         type_diagnostic = TypeDiagnostic.objects.filter(name=self.request.data['name'], deleted=0).exclude(id=self.kwargs['pk'])          
    #     except:
    #         type_diagnostic = None
    #     if type_diagnostic:
    #         raise ValidationError({'name': ['Ya se registró este diagnostico.']})              
    #     serializer.save()

    
    def perform_destroy(self, serializer): 

        errors = {}
        parents = ParentsChilds.objects.filter(parent=self.kwargs['pk'])
        if parents:
            errors['error'] = 'Esta persona ya tiene un menor asociado por lo tanto no puede eliminarse.'
        if errors:
            raise ValidationError(errors)
        serializer.delete()


class ParentsFullDataViewSet(BaseViewSet):
    '''
    Parent's full data view
    FILTROS:
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
    '''
    permission_code = 'parents'
    
    queryset = Parents.objects.all().select_related('created_by','updated_by').order_by('document', 'name')
    serializer_class = ParentsFullDataSerializer
    filter_class = ParentsFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
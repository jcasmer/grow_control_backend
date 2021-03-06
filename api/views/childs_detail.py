'''
'''
from datetime import datetime

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import ChildsDetail
from ..serializers import ChildsDetailSerializer, ChildsDetailFullDataSerializer
from ..filters import ChildsDetailFilter, ChildsDetailFullDataFilter


class ChildsDetailViewSet(BaseViewSet):
    '''
    Parent's view
    FILTERS:
        'id': ['exact'],
        'child__document': ['exact', 'icontains'],
        'child__name': ['exact', 'icontains'],
        'height': ['exact', 'icontains'],
        'weight': ['exact','icontains']        
    '''
    permission_code = 'childsdetail'
    
    queryset = ChildsDetail.objects.all().select_related('created_by','updated_by')
    serializer_class = ChildsDetailSerializer
    filter_class = ChildsDetailFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)


    def perform_create(self, serializer):  # pylint: disable=arguments-differ
        '''
        Overwrite create
        '''   
        try:
            detail = ChildsDetail.objects.filter(created_at__lte=datetime.now(), deleted=0, child_id=self.request.data['child']).last()
        except:
            detail = None
        # if detail:
        #     raise ValidationError({'error': ['Solo se puede registrar un control por día.']})              
        serializer.save()   


class ChildsDetailFullDataViewSet(BaseViewSet):
    '''
    Parent's full data view
    FILTROS:
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
    '''
    permission_code = 'childsdetail'
    
    queryset = ChildsDetail.objects.all().select_related('created_by','updated_by').order_by('-created_at')
    serializer_class = ChildsDetailFullDataSerializer
    filter_class = ChildsDetailFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
'''
'''

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..models import Childs, ChildsDetail
from ..serializers import ChildsSerializer, ChildsFullDataSerializer
from ..filters import ChildsFilter, ChildsFullDataFilter


class ChildsViewSet(BaseViewSet):
    '''
    Parent's view
    FILTERS:
        'id': ['exact'],
        'name':['exact', 'icontains'],
        'document': ['exact', 'icontains'],
        'gender': ['exact'],
        'date_born': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],      
    '''
    permission_code = 'childs'
    
    queryset = Childs.objects.all().select_related('created_by','updated_by')
    serializer_class = ChildsSerializer
    filter_class = ChildsFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    
    def perform_destroy(self, serializer): 

        errors = {}
        try:
            child_details = ChildsDetail.objects.filter(child=self.kwargs['pk'])
            if child_details:
                for child in child_details:
                    child.delete()
        except:
            pass
      
        serializer.delete()


class ChildsFullDataViewSet(BaseViewSet):
    '''
    Parent's full data view
    FILTROS:
        'id': ['exact'],
        'name':['exact', 'icontains'],
        'document': ['exact', 'icontains'],
        'gender': ['exact'],
        'date_born': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'created_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'created_by__username': ['exact', 'icontains'],
        'updated_at': ['exact', 'year', 'year__gte', 'year__lte', 'month', 'month__lte', 'month__gte', 'day', 'day__lte', 'day__gte', 'year__in', 'month__in', 'day__in'],
        'updated_by__username': ['exact', 'icontains'],  
    '''
    permission_code = 'childs'
    
    queryset = Childs.objects.all().select_related('created_by','updated_by').order_by('document', 'name')
    serializer_class = ChildsFullDataSerializer
    filter_class = ChildsFullDataFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend)
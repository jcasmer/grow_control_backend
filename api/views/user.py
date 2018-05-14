'''
'''

from django.contrib.auth.models import User, Group

from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import  DjangoFilterBackend

from src.base_view import BaseViewSet

from ..serializers import UserSerializer, UserFullDataSerializer
from ..filters import UserFilter, UserFullDataFilter


class UserViewSet(BaseViewSet):
    '''
    Vista maestro de usuarios
    FILTROS:
        username: coicidencia o valor exacto
        first_name: coicidencia o valor exacto
        last_name: coicidencia o valor exacto
        is_active: valor exacto
    '''
    permission_code = 'user'

    queryset = User.objects.all().prefetch_related('groups')
    serializer_class = UserSerializer
    filter_class = UserFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    

class UserFullDataViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    permission_code = 'user'
    queryset = User.objects.all().prefetch_related('groups').order_by('username')
    serializer_class = UserFullDataSerializer
    filter_class = UserFullDataFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)

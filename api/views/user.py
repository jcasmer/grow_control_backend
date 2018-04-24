'''
'''
import re

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from django.core.validators import validate_email

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
   # ordering_fields = ('username', 'email')

    def perform_create(self, serializer):
        '''
        método para crear usuarios
        '''
        errors = {}
        if not self.request.data['first_name']:
            errors['first_name'] = ['Este campo no puede estar en blanco.']
        if not self.request.data['last_name']:
            errors['last_name'] = ['Este campo no puede estar en blanco.']
        if errors:
            raise ValidationError(errors)
        try:            
            user = User.objects.get(username=self.request.data['username'])
            errors['username'] = ['Este usuario ya se encuentra registrado.']
        except ObjectDoesNotExist:           
            super().perform_create(serializer)
            user = User.objects.get(username=self.request.data['username']) 
            user.is_superuser = True
            user.save()
        if errors:
            raise ValidationError(errors)

    def perform_update(self, serializer):
        '''
        método para actualizar usuarios
        '''
        errors = {}
        if not self.request.data['first_name']:
            errors['first_name'] = ['Este campo no puede estar en blanco.']
        if not self.request.data['last_name']:
            errors['last_name'] = ['Este campo no puede estar en blanco.']
        if errors:
            raise ValidationError(errors)
            
        try:
            user = User.objects.filter(username=self.request.data['username']).exclude(id=self.kwargs['pk'])
            if user:
                errors['username'] = ['Este usuario ya se encuentra registrado.']
            else:
                serializer.save()
                user = User.objects.get(username=self.request.data['username'])
                user.is_superuser = True
                user.save()
        except Exception as e:
            errors['error'] = [e]
        
        if errors:
            raise ValidationError(errors)


class UserFullDataViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    permission_code = 'user'
    queryset = User.objects.all().prefetch_related('groups')
    serializer_class = UserFullDataSerializer
    filter_class = UserFullDataFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)
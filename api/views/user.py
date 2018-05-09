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
   # ordering_fields = ('username', 'email')

    def perform_create(self, serializer):
        '''
        método para crear usuarios
        '''
        errors = {}
        if self.request.data['password'] and len(self.request.data['password']) < 8:
            errors['password'] = ['La contraseña debe tener mínimo 8 caractres']
        if not self.request.data['group']:
            errors['group'] = ['Este campo no puede ser nulo']
        user = User.objects.filter(username=self.request.data['username']).exclude(id=self.kwargs['pk'])
        if user:
            errors['username'] = ['El usuario ya existe']
        if errors:
            raise ValidationError(errors)
        group_id = self.request.data.get('group')
        group = Group.objects.get(id=group_id)            
        super().perform_create(serializer)
        user = User.objects.get(username=self.request.data['username'])
        user.groups.add(group)
        user.save()
        

    def perform_update(self, serializer):
        '''
        método para actualizar usuarios
        '''
        errors = {}
        user = User.objects.filter(username=self.request.data['username']).exclude(id=self.kwargs['pk'])
        if user:
            errors['username'] = ['El usuario ya existe']
        if self.request.data['password'] and len(self.request.data['password']) < 8:
            errors['password'] = [
                'La contraseña debe tener mínimo 8 caracteres']
        if not self.request.data['group']:
            errors['group'] = ['Este campo no puede ser nulo']
        if errors:
            raise ValidationError(errors)
        serializer.save()
        user = User.objects.get(username=self.request.data['username'])
        group_id = self.request.data.get('group')
        group_user = Group.objects.get(id=group_id)
        groups = Group.objects.all()
        for group in groups:
            group.user_set.remove(user)
        user.groups.add(group_user)
        user.save()



class UserFullDataViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    permission_code = 'user'
    queryset = User.objects.all().prefetch_related('groups')
    serializer_class = UserFullDataSerializer
    filter_class = UserFullDataFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter)

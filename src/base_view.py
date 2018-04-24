# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group, User, Permission

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.response import Response


def validate_permission(type, permission_code, request):
    try:
        permission_name_user = '{}.{}_{}'.format('auth', type, permission_code)
        permission_name_app = '{}.{}_{}'.format('api', type, permission_code)
        
        if permission_code == 'user': 
            if not request.user.has_perm(permission_name_user):
                return Response({'detail': 'Acceso inválido.'}, status=403)
        elif not request.user.has_perm(permission_name_app):
            return Response({'detail': 'Acceso inválido.'}, status=403)
    except AttributeError: 
        return Response({'detail': 'Acceso inválido.'}, status=403)
    except Exception:
        return Response({'detail': 'Error inesperado validando permisos.'}, status=402)

    return True


class BaseViewSet(viewsets.ModelViewSet):

    def initialize_request(self, request, *args, **kwargs):
        return super().initialize_request(request, *args, **kwargs)

    def list(self, request):
        permission = validate_permission('list', self.permission_code, request)
        if not permission is True:
            return permission
            
        if request.GET.get('nopaginate'):
            self.pagination_class = None
        return super().list(request)
    
    def create(self, request):
        permission = validate_permission('add', self.permission_code, request)
        if not permission is True:
            return permission

        return super().create(request)
     
    def retrieve(self, request, pk=None):
        permission = validate_permission('retrieve', self.permission_code, request)
        if not permission is True:
            return permission
         
        return super().retrieve(request, pk)
    
    def update(self, request, pk=None):
        permission = validate_permission('change', self.permission_code, request)
        if not permission is True:
            return permission

        return super().update(request, pk)
     
    def partial_update(self, request, pk=None):
        permission = validate_permission('change', self.permission_code, request)
        if not permission is True:
            return permission
          
        return super().partial_update(request, pk)
     
    def destroy(self, request, pk=None):
        permission = validate_permission('delete', self.permission_code, request)
        if not permission is True:
            return permission
        
        return super().destroy(request, pk)
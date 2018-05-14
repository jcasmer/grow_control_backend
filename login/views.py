# pylint: disable=C0111
'''
Vista del archivo login
'''

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


class LoginView(APIView):
    '''
    Metodo para iniciar sesión.
    '''

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        errors = {}

        username = request.data.get('username')
        password = request.data.get('password')

        if not username :
            errors['username'] = ['El campo usuario es obligatorio.']
        if not password:
            errors['password'] = ['El campo contraseña es obligatorio.']

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username, is_active=True)
        except ObjectDoesNotExist:
            return Response({'detail': ['Acceso denegado']}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            user_authenticated = authenticate(username=username, password=password)
            if user_authenticated and user.is_active:
                login(request, user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            code_permissions = []
            try:
                permissions = Permission.objects.filter(user=user) | Permission.objects.filter(group__user=user)            
                for permission in permissions:
                    code_permissions.append(permission.codename)
            except:
                pass
            group_permissions = []
            groups = Group.objects.filter(user=user)
            for group in groups:
                group_permissions.append(group.name)
            full_name = user.first_name + ' ' + user.last_name if user.first_name and user.last_name else ''
            return Response({'token': token,'username': user.username, 'full_name': full_name , 'is_superuser': user.is_superuser, 'permissions': code_permissions, 'groups':group_permissions}, status=status.HTTP_202_ACCEPTED)
        except Token.DoesNotExist:
            return Response({'detail': ['Acceso denegado']}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'detail': ['Actualmente no se puede ingresar a la aplicación, por favor intente más tarde']}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    '''
    Metodo para cerrar la sesión.
    '''

    def get(self, request):

        token_number = request.META.get('Autorization').split(' ')[1]
        try:
            token = Token.objects.get(key=token_number)
            user = token.user
            token.delete()

            Token.objects.create(user=user)
        except Token.DoesNotExist:
            return Response({'detail':['Token incorrecto']}, status=status.HTTP_401_UNAUTHORIZED)

        response = Response({}, status=status.HTTP_202_ACCEPTED)
        return response
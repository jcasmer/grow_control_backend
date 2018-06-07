'''
'''

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.db import transaction

from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import Childs, Parents, ParentsChilds
from ..serializers import ChidlsSerializer, ParentsSerializer


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes(['add_childs'])
def RegistrationChildView(request):
    
    data = request.data
    data_child= data[0]['child']
    data_parents =  data[0]['parents']

    

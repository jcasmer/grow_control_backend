'''
'''
import re

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

from api.models import Parents, Relationship


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def ValidateParentsView(request):
    
    try:
        errors = {}
        if 'document' not in request.GET:
            errors['document'] = ['Debe ingresar el documento.']
        if 'relationship' not in request.GET:
            errors['relationship'] = ['Debe ingresar el parentesco.']
        if errors:
            return Response(errors, status=400)
    except:
        return Response({'document': ['Debe ingresar el documento.']}, status=400)

    if not re.match('^[0-9]+$', request.GET['document']) and request.GET['document']:
        return Response({'document': ['Este campo debe ser numérico.']}, status=400)
    try:
        parents = Parents.objects.get(document=request.GET['document'])
    except:
        return Response({'document': ['No se encontró la persona con el documento indicado.']}, status=400)
    try:
        relationship = Relationship.objects.get(id=request.GET.get('relationship'))
    except:
        pass
    data = {}
    try:
        data['id'] = parents.id
        data['document'] = parents.document
        data['name'] = parents.name
        data['relationship'] = relationship.name
    except Exception as e:
        return Response({'errors': 'No se encontró la persona  con el documento indicado.'}, status=400)
    
    return Response(data, status=200)

    

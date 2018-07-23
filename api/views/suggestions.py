'''
'''
from datetime import datetime
import math
import locale

from django.conf import settings
from django.db import transaction
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import Advices, TypeDiagnostic


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def SuggestionsView(request):
    
    if 'status' not in request.GET or not request.GET.get('status'):
        return Response({'error': 'No se encontraron recomendaciones. Contacte al administrador'}, status=400)
    try:
        diagnostic = TypeDiagnostic.objects.get(name=request.GET.get('status'))
    except:
        return Response({'error': 'No se encontraron recomendaciones. Contacte al administrador'}, status=400)

    advices = Advices.objects.filter(type_diagnostic=diagnostic).order_by('id')
    if not advices:
        return Response({'error': 'No se encontraron recomendaciones. Contacte al administrador'}, status=400)
    data = []
    i = 1
    for advice in advices:
        data.append({'id': i, 'description': advice.description})
        i += 1
    full_data = {
        'advices': data
    }
    return Response(full_data, status=200)


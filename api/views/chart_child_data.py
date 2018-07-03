'''
'''
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

from api.models import Childs, ChildsDetail
from lib.utilities import Utilites


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def ChartChildDataView(request):
    
    full_data = {}
    label = []
    data = []
    childs_detail = None
    if 'idChild' in request.GET:
        childs_detail = ChildsDetail.objects.filter(child=request.GET.get('idChild')).order_by('created_at')
        
    else:
        return Response({'error': 'No se encontró el registro'}, status=400)
    # if 'document' in request.GET and not:
    #     childs_detail = ChildsDetail.objects.filter(child__document=request.GET.get('document')).order_by('created_at')
    # else:
    #     return Response({'error': 'No se encontró controles realizados para el menor'}, status=400)

    if not childs_detail:
        return Response({'error': 'No se encontró controles realizados para el menor'}, status=400)
    
    try:
        child = Childs.objects.get(id=request.GET.get('idChild'))
    except:
        pass
    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
    label.append('Semana: '+ ' ' + child.date_born.strftime('%u') + ' año: ' + child.date_born.strftime('%Y'))
    if request.GET.get('chartType') == '1':
        data.append(child.weight_born)
    elif request.GET.get('chartType') == '2':
        data.append(child.height_born)

    for detail in childs_detail:
        label.append('Semana: '+ ' ' + detail.created_at.strftime('%U') + ' año: ' + detail.created_at.strftime('%Y'))
        # type 1 == weight 
        if request.GET.get('chartType') == '1':
            data.append(detail.weight)
        elif request.GET.get('chartType') == '2':
            data.append(detail.height)

    full_data = {
        'label': label,
        'data': data
    }
    return Response(full_data, status=200)


    

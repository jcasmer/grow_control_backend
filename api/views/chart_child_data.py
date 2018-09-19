'''
'''
from datetime import datetime
import math
import locale

from django.conf import settings
from django.db import transaction
from django.contrib.auth.models import User
from django.db.models import Max

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
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def ChartChildDataView(request):
    
    full_data = {}
    label = []
    data = []
    childs_detail = None

    if 'idChild' in request.GET:
        childs_detail = ChildsDetail.objects.filter(child=request.GET.get('idChild')).annotate(created_at_max=Max('created_at')).order_by('created_at')       
    else:
        return Response({'error': 'No se encontró el registro'}, status=400)

    if not childs_detail:
        return Response({'error': 'No se han realizado controles para el menor'}, status=400)
    
    try:
        child = Childs.objects.get(id=request.GET.get('idChild'))
    except:
        pass
    locale.setlocale(locale.LC_TIME, 'es_CO.utf8')
    label.append('0')
    if request.GET.get('chartType') == '1':
        data.append(child.weight_born)
    elif request.GET.get('chartType') == '2':
        data.append(child.height_born)
    
    week = None
    for detail in childs_detail:
        
        date_to_subs = detail.created_at - datetime.combine(child.date_born, datetime.min.time())
        if request.GET.get('chartType') == '2':
            week = math.ceil(date_to_subs.days / 30 )
        else:
            week = math.ceil(date_to_subs.days / 7 )
        # type 1 == weight 
        label.append(week)
        if request.GET.get('chartType') == '1':
            data.append(detail.weight)
        # type 2 == height 
        elif request.GET.get('chartType') == '2':
            data.append(detail.height)
        # type 3 == IMC 
        elif request.GET.get('chartType') == '3':
            imc = child.weight_born / child.height_born * child.height_born
            data.append(imc)
            imc = detail.weight / detail.height * detail.height
            data.append(imc)
    maxlenght = len(childs_detail) - 1
    date_to_subs = childs_detail[maxlenght].created_at - datetime.combine(child.date_born, datetime.min.time())
    date_to_subs = math.ceil(date_to_subs.days / 7 )
    

    childs_detail2 = ChildsDetail.objects.filter(child=request.GET.get('idChild')).last()
    child_status = Utilites.get_child_status(child.gender, request.GET.get('chartType'), childs_detail2, date_to_subs )
    oms_data = Utilites.get_oms_data(child.gender, request.GET.get('chartType'), week )
    full_data = {
        'label': label,
        'data': data,
        'oms': oms_data,
        'status': child_status
    }
    return Response(full_data, status=200)


    

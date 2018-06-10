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

from api.models import Childs, Parents, ParentsChilds, Relationship
from ..serializers import ChildsSerializer, ParentsSerializer


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def RegistrationChildView(request):
    
    data = request.data
    data_child= data[0]['child']
    data_parents =  data[0]['parents']
    form_child = ChildsSerializer(data=data_child, context={'request': request})
    try:
        validate_parent = Parents.objects.get(document=data_child['document'])
        if validate_parent:
            return Response({'error': ['El documento del menor ingresado se encuentra registrado como un responsable.']}, status=400)
    except:
        pass
    if not form_child.is_valid():
        return Response(form_child.errors, status=400)
    try:
        with transaction.atomic():
            form_child.save()
            if data_parents:
                for parents in data_parents:
                    parent_id = Parents.objects.get(documment=parents['document'])
                    relationship_id = Relationship.objects.get(name=parents['relationship'], is_active=true)
                    parents_childs = ParentsChilds(child=form_child, parent=parent_id, relationship=relationship_id)
                    parents_childs.save()
                    
    except ValueError as e:
        transaction.rollback()
        return Response({'error': str(e)}, status=400)
    except Exception as e:
        transaction.rollback()
        return Response({'error': 'Se ha presentado error con el registro'}, status=400)

    return Response('', status=200)


    

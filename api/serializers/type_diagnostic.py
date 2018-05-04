
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.conf import settings

from ..models import TypeDiagnostic, IS_ACTIVE_TYPE
from ..serializers import UserFullDataSerializer


class TypeDiagnosticSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeDiagnostic
        fields = ('url', 'id', 'name', 'is_active')        
       
        

class TypeDiagnosticFullDataSerializer(serializers.ModelSerializer):
    
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    is_active_display = serializers.CharField(source='get_is_active_display')
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = TypeDiagnostic
        fields = ('url', 'id','name', 'is_active', 'is_active_display', 'created_at', 'created_by', 'updated_at', 'updated_by')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_by': {'read_only': True},
            'updated_by': {'read_only': True},
        }

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import TypeDiagnostic, IS_ACTIVE_TYPE
from ..serializers import UserSerializer


class TypeDiagnosticSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeDiagnostic
        fields = ('url', 'id', 'name', 'is_active')        
       
        

class TypeDiagnosticFullDataSerializer(serializers.ModelSerializer):
    
    created_by = UserSerializer()
    updated_by = UserSerializer()
    is_active_display = serializers.CharField(source='get_is_active_display')

    class Meta:
        model = TypeDiagnostic
        fields = ('url', 'id','name', 'is_active', 'is_active_display', 'created_at', 'created_by', 'updated_at', 'updated_by')
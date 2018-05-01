
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import TypeDiagnostic
from ..serializers import UserSerializer


class TypeDiagnosticSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeDiagnostic
        fields = ('url', 'id', 'name', 'is_active')        
       
        

class TypeDiagnosticFullDataSerializer(serializers.ModelSerializer):
    
    created_by = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = TypeDiagnostic
        fields = ('url', 'id','name', 'is_active', 'created_at', 'created_by', 'updated_at', 'updated_by')
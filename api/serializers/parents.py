
from rest_framework import serializers
from django.conf import settings

from ..models import Parents


class ParentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = ('url', 'id', 'document_type', 'document', 'name', 'age', 'gender', 'relationship',
                'phone_number', 'email', 'social_stratum', 'height', 'weight', 'is_active')        
       

class ParentsFullDataSerializer(serializers.ModelSerializer):
    
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    document_type = serializers.CharField(source='get_document_type_display')
    gender = serializers.CharField(source='get_gender_display')
    social_stratum = serializers.CharField(source='get_social_stratum_display')
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Parents
        fields = ('url', 'id', 'document_type', 'document', 'name', 'age', 'gender', 'relationship',
                'phone_number', 'email', 'social_stratum', 'height', 'weight', 'is_active', 'created_by',
                'created_at', 'updated_by', 'updated_at')
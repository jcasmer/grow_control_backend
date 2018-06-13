
from rest_framework import serializers
from django.conf import settings

from ..models import ParentsChilds


class ParentsChildsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentsChilds
        fields = ('url', 'id', 'parent', 'child', 'relationship')        
       
        

class ParentsChildsFullDataSerializer(serializers.ModelSerializer):
    
    parent_document = serializers.ReadOnlyField()
    parent = serializers.StringRelatedField()
    child = serializers.StringRelatedField()
    relationship = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = ParentsChilds
        fields = ('url', 'id', 'parent', 'child', 'relationship', 'parent_document', 'created_at', 'created_by', 'updated_at', 'updated_by')
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'created_by': {'read_only': True},
            'updated_by': {'read_only': True},
        }
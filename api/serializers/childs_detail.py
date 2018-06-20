
from rest_framework import serializers
from django.conf import settings

from ..models import ChildsDetail


class ChildsDetailSerializer(serializers.ModelSerializer):

    # age = serializers.ReadOnlyField()

    class Meta:
        model = ChildsDetail
        fields = ('url', 'id', 'child', 'height', 'weight',)
        

class ChildsDetailFullDataSerializer(serializers.ModelSerializer):
    
    child = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = ChildsDetail
        fields = ('url', 'id', 'child', 'height', 'weight',
            'created_by', 'created_at', 'updated_by', 'updated_at')

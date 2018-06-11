
from rest_framework import serializers
from django.conf import settings

from ..models import Childs


class ChildsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Childs
        fields = ('url', 'id', 'document', 'name', 'gender', 'date_born')   


class ChildsSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Childs
        fields = ('id', 'document', 'name', 'gender', 'date_born')   


class ChildsFullDataSerializer(serializers.ModelSerializer):
    
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    gender = serializers.CharField(source='get_gender_display')
    date_born = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Childs
        fields = ('url', 'id', 'document', 'name', 'gender', 'date_born', 'age', 'created_by',
                'created_at', 'updated_by', 'updated_at')

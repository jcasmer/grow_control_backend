
from django.contrib.auth.models import Group, Permission

from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ('url', 'id', 'name', 'codename' )
        

class GroupSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Group
        fields = ('url', 'id', 'name' )
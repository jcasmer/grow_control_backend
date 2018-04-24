import re

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from rest_framework import serializers

from ..serializers.group import GroupSerializer


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if validated_data.get('password'):
            user.set_password(validated_data.get('password'))
        user.save()
        return user

    class Meta:

        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',)
        extra_kwargs = {
            'username': {
                'validators': [
                    validators.RegexValidator(
                        r'^[\w.@+-]+$',
                        _(' Sólo debe contener letras, números y los caracteres:' ' @.+-_ ')
                    ), ]
            }
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name',)

        
class UserFullDataSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'date_joined')
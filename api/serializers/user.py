
import re

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from django.contrib.auth.models import Group, User

from rest_framework import serializers

from ..serializers.group import GroupSerializer


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(label='Correo electrónico', required=True, allow_null=False)
    first_name = serializers.CharField(label='Nombre(s)', required=True, allow_null=False)
    last_name = serializers.CharField(label='Apellido(s)', required=True, allow_null=False)
    password = serializers.CharField(label='Contraseña', required=True, allow_null=False, style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(label='Confirme contraseña', required=False, allow_null=True, allow_blank=True, style={'input_type': 'password'}, write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'data' in kwargs:
            if 'partial' in kwargs:
                self.fields['password'].required = False
                self.fields['password'].allow_blank = True
                self.fields['confirm_password'].required = False
                self.fields['confirm_password'].allow_blank = True
            else:
                self.fields['password'].required = True
                self.fields['password'].allow_blank = False
                self.fields['password'].allow_null = False
                self.fields['confirm_password'].required = True
                self.fields['confirm_password'].allow_blank = False
                self.fields['confirm_password'].allow_null = False


    def create(self, validated_data):

        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        # user.set_password(validated_data.get('password'))
        user.save()
        return user

    class Meta:

        model = User
        fields = ('url', 'id', 'username', 'password', 'confirm_password', 'first_name',
                  'last_name', 'email', 'is_active', 'is_superuser', 'is_staff', 'groups')
        extra_kwargs = {
            'username': {
                'validators': [
                    validators.RegexValidator(
                        r'^[\w.@+-]+$',
                        _('Ingrese un usuario válido.'
                          ' Sólo debe contener letras, números y los caracteres:' ' @.+-_ ')
                    ), ]
            }
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name',)

class UserFullDataSerializer(serializers.ModelSerializer):

    groups = GroupSerializer(many=True)
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name', 'last_name',
                  'email', 'is_active', 'groups')
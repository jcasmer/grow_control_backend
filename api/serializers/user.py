
import re

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import Group, User

from rest_framework.exceptions import ValidationError
from rest_framework import serializers

# from ..serializers.group import GroupSerializer

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(label='Correo electrónico', required=True, allow_null=False)
    first_name = serializers.CharField(label='Nombre(s)', required=True, allow_null=False)
    last_name = serializers.CharField(label='Apellido(s)', required=True, allow_null=False)
    password = serializers.CharField(label='Contraseña', required=True, allow_null=False, style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(label='Confirme contraseña', required=False, allow_null=True, allow_blank=True, style={'input_type': 'password'}, write_only=True)
    groups = serializers.CharField(write_only=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'data' in kwargs:
            if 'partial' in kwargs:
                
                if kwargs['data']['changePassword']:
                    self.fields['password'].allow_null = False    
                    self.fields['confirm_password'].allow_null = False
                    self.fields['password'].required = True
                    self.fields['password'].allow_blank = False
                    self.fields['confirm_password'].required = True
                    self.fields['confirm_password'].allow_blank = False
                else:
                    self.fields['password'].allow_null = True    
                    self.fields['confirm_password'].allow_null = True
                    self.fields['password'].required = False
                    self.fields['password'].allow_blank = True
                    self.fields['confirm_password'].required = False
                    self.fields['confirm_password'].allow_blank = True
            else:
                self.fields['password'].required = True
                self.fields['password'].allow_blank = False
                self.fields['password'].allow_null = False
                self.fields['confirm_password'].required = True
                self.fields['confirm_password'].allow_null = False
                self.fields['confirm_password'].allow_blank = False

    def validate(self, data):
        errors = {}
        if self.instance:
            user = User.objects.filter(username=data.get('username')).exclude(id=self.instance.id)
            if user:
                errors['username'] = ['El usuario ya existe']
        else:
            user = User.objects.filter(username=data.get('username'))
            if user:
                errors['username'] = ['El usuario ya existe']
        if data.get('password') and len(data.get('password')) < 8:
            errors['password'] = ['La contraseña debe tener mínimo 8 caracteres.']
        if data.get('confirm_password') and len(data.get('confirm_password')) < 8:
            errors['confirm_password'] = ['La contraseña debe tener mínimo 8 caracteres.']
        if not data.get('groups'):
            errors['groups'] = ['Este campo no puede ser nulo']
        if data.get('password') != data.get('confirm_password'):
            errors['password'] = ['Las contraseñas no coinciden.']
            errors['confirm_password'] = ['Las contraseñas no coinciden.']
        if errors:
            raise ValidationError(errors)
        
        return data


    def create(self, validated_data):
        try:
            groups_data = validated_data.pop('groups')
            group = Group.objects.get(id=groups_data)
        except Exception as e:
            group = None
        try:
            validated_data.pop('confirm_password')
        except:
            pass
        user = User.objects.create_user(**validated_data)
        user.groups.add(group)
        if group.name == 'Administrador':
            user.is_staff = True
            user.is_superuser= True
            user.save()
        return user

    def update(self, instance, validated_data):

        errors = {}
        user = User.objects.filter(username=validated_data.get('username')).exclude(id=instance.id)

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        try:
            group = Group.objects.get(id=validated_data['groups'])
        except Exception as e:
            group = None
        groups = Group.objects.all()
        for group_remove in groups:
            group_remove.user_set.remove(instance)
        instance.groups.add(group)
        if group.name == 'Administrador':
            instance.is_staff = True
            instance.is_superuser= True
        else:
            instance.is_staff = False
            instance.is_superuser= False
        try:    
            if validated_data['confirm_password']:
                instance.set_password(validated_data['confirm_password'])
        except:
            pass
        
        
        instance.save()
        return instance

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
            
       
class UserFullDataSerializer(serializers.ModelSerializer):

    group_name = serializers.SerializerMethodField()

    def get_group_name(self, obj):
        return obj.groups.get().name
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'is_active', 'is_superuser', 'is_staff', 'groups', 'group_name')
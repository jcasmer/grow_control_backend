
import re

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from django.contrib.auth.models import Group, User

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

    def create(self, validated_data):
        # user = super().create(validated_data)
        # groups_data = validated_data.pop('groups')
        erros = {}
        user = User.objects.filter(username=validated_data.get('username'))
        if user:
            errors['username'] = ['El usuario ya existe']
        if validated_data.get('password') and len(validated_data.get('password')) < 8:
            errors['password'] = ['La contraseña debe tener mínimo 8 caracteres']
        if validated_data.get('confirm_password') and len(validated_data.get('confirm_password')) < 8:
            errors['confirm_password'] = ['La contraseña debe tener mínimo 8 caracteres']
        if not validated_data.get('groups'):
            errors['groups'] = ['Este campo no puede ser nulo']
        if validated_data.get('password') != validated_data.get('confirm_password'):
            raise serializers.ValidationError({'confirm_password': ['Las contraseñas o coinciden.']})
        if errors:
            raise ValidationError(errors)
        try:
            group = Group.objects.get(id=validated_data.get('groups'))
        except:
            group = None
        user = User.objects.create_user(**validated_data)   
        user.groups.add(group)
        if group.name == 'Administrador':
            user.is_staff = True
            user.is_superuser= True
            user.save()
        # user.set_password(validated_data.get('password'))
        # user.save()
        return user

    def update(self, instance, validated_data):
        print('ss')
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
            
       
class UserFullDataSerializer(serializers.ModelSerializer):

    group_name = serializers.SerializerMethodField()

    def get_group_name(self, obj):
        return obj.groups.get().name
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'is_active', 'is_superuser', 'is_staff', 'groups', 'group_name')
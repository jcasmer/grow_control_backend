import django_filters

from django.contrib.auth.models import User


class UserFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['icontains', 'exact'],
            'first_name': ['icontains', 'exact'],
            'last_name': ['icontains', 'exact'],
            'email': ['icontains', 'exact'],
            'is_active': ['exact']
        }
        ordering_fields = ('username', 'first_name', 'last_name')


class UserFullDataFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['icontains', 'exact'],
            'first_name': ['icontains', 'exact'],
            'last_name': ['icontains', 'exact'],
            'is_active': ['exact'],
            'email': ['icontains', 'exact']
        }
        ordering_fields = ('username', 'first_name', 'last_name')
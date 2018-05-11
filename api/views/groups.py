'''
'''

from django.contrib.auth.models import Group, Permission

from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from ..serializers import GroupSerializer

from src.base_view import BaseViewSet

class GroupsFullDataViewSet(BaseViewSet):
    '''
    VieSet para grupos
    '''
    permission_code = 'user'
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # filter_class = GroupFilter
    # search_fields = ('name', 'permissions__codename')
    ordering_fields = ('name',)

    def list(self, request):
        self.permission_code = None
        return super().list(request)

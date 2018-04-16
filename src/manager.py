'''
Clases base para ORM.
'''

from django.db import models


class CustomManager(models.Manager):
    '''
    Manager para los query a ejecutar.
    Todos los modelos del framework usaran este manager para hacer los query a
    la base de datos, este ajustará automáticamente los query simples con el
    valor deleted=False para evitar traer elementos eliminados.
    '''

    def get_queryset(self):
        '''
        Retorna los query con filtro deleted=False en cada query ejecutado.
        '''

        return super().get_queryset().filter(deleted=False)
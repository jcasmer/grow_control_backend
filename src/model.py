'''
Base model
'''
import datetime

from django.db import models
from django.contrib.auth.models import User

from src.middleware import current_request
from src.manager import CustomManager


class BaseModel(models.Model):
    '''
    Base model's fields
    '''

    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Fecha de modificación', null=True)
    created_by = models.ForeignKey(
        User, verbose_name='Creado por', related_name='%(app_label)s_%(class)s_created_by', on_delete=models.PROTECT,)
    updated_by = models.ForeignKey(
        User, verbose_name='Modificado por', related_name='%(app_label)s_%(class)s_updated_by', on_delete=models.PROTECT, null=True)
    deleted = models.BooleanField('Eliminado', default=False)

    objects = CustomManager()

    def delete(self):
        '''
        Override delete method with logic elimination.
        '''
        self.deleted = True
        self.save()

    def save(self, *args, **kwargs):
        '''
        Override save method with register and updater user.
        '''

        request = current_request()
        # Validar si se esta creando o editando.
        if self._state.adding:
            self.created_by = request.current_request.user
            self.created_at = datetime.datetime.today()
        else:
            try:
                self.updated_by = request.current_request.user
            except:
                pass
            self.updated_at = datetime.datetime.today()

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
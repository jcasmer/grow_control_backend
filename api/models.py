from django.db import models
from src.model import BaseModel

# Create your models here.

class TypeDiagnostic(BaseModel):
    '''
    Model to save the types of childs state like thin, fat etc.
    '''
    
    name = models.CharField('Tipo Diagnostico', max_length=150)

    def __str__(self):
        return self.name


class Relationship(BaseModel):
    '''
    Model where find kind of relationship parents has to childs
    '''

    name = models.CharField('Parentesco', max_length=150)

    def __str__(self):
        return self.name


class Advices(BaseModel):
    '''
    Model that contains all the advices/recomendations per diagnostics
    '''

    description = models.TextField('Descripción')
    type_diagnostic = models.ForeignKeyField(TypeDiagnostic, verbose_name='Tipo de Diagnostico')

    def __str__(self):
        return self.description


class Parents(BaseModel):
    '''
    Model's parents (parents detail)
    '''
    DOCUMENT_TYPE = (
        ('Cedula', 'Cédula'),
        ('Cedula Extranjeria', 'Extranjería'),
    )

    document_type = models.CharField(s)
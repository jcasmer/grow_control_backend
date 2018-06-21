# -*- coding: utf-8 -*-
from datetime import date

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

from lib.validators import isnumbervalidator
from src.model import BaseModel

GENDER_TYPE = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)

IS_ACTIVE_TYPE = (
    (True, 'Activo'),
    (False, 'Inactivo')
)

UNIQUE_DOCUMENT_MESSAGE = 'Est documento ya se encuentra registrado.'

class TypeDiagnostic(BaseModel):
    '''
    Model to save the types of childs state like thin, fat etc.
    '''
    name = models.CharField('Tipo Diagnostico', max_length=150)
    is_active = models.BooleanField('Estado', choices=IS_ACTIVE_TYPE)

    def __str__(self):
        return self.name


class Relationship(BaseModel):
    '''
    Model where find kind of relationship parents has to childs
    '''

    name = models.CharField('Parentesco', max_length=150)
    is_active = models.BooleanField('Estado', choices=IS_ACTIVE_TYPE)
    
    def __str__(self):
        return self.name


class Advices(BaseModel):
    '''
    Model that contains all the advices/recomendations per diagnostics
    '''

    description = models.TextField('Descripción')
    type_diagnostic = models.ForeignKey(TypeDiagnostic, verbose_name='Tipo de Diagnostico', on_delete=models.PROTECT)
    is_active = models.BooleanField('Estado', choices=IS_ACTIVE_TYPE)
    
    def __str__(self):
        return self.description


class Parents(BaseModel):
    '''
    Model's parents (parents information)
    '''

    DOCUMENT_TYPE = (
        ('Cédula', 'Cédula'),
        ('Cédula Extranjería', 'Cédula Extranjería'),
    )
    
    SOCIAL_STRATUM_TYPE = (
        ('0', 'Estrato 0'),
        ('1', 'Estrato 1'),
        ('2', 'Estrato 2'),
        ('3', 'Estrato 3'),
        ('4', 'Estrato 4'),
        ('5', 'Estrato 5'),
        ('6', 'Otro'),
    )

    document_type = models.CharField('Tipo de documento', max_length=100, choices=DOCUMENT_TYPE)
    document = models.CharField('Documento', max_length=20, unique=True, 
            error_messages={'unique': UNIQUE_DOCUMENT_MESSAGE}, validators=[isnumbervalidator, MinLengthValidator(6)])
    name = models.CharField('Nombre', max_length=150)
    age = models.IntegerField('Edad', validators=[MinValueValidator(1)])
    gender = models.CharField('Genero', max_length=50, choices=GENDER_TYPE)
    phone_number = models.CharField('Teléfono', max_length=20, validators=[isnumbervalidator, MinLengthValidator(10)])
    email = models.EmailField('Correo Electrónico')
    social_stratum = models.CharField('Estrato', max_length=3, choices=SOCIAL_STRATUM_TYPE)
    height = models.FloatField('Altura', validators=[MinValueValidator(1)])
    weight = models.FloatField('Peso', validators=[MinValueValidator(1)])
    is_active = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.name

class Childs(BaseModel):
    '''
    Model's childs (childs information)
    '''
    document = models.CharField('Documento', max_length=20, unique=True, error_messages={'unique': UNIQUE_DOCUMENT_MESSAGE})
    name = models.CharField('Nombre', max_length=150)
    gender = models.CharField('Genero', max_length=50, choices=GENDER_TYPE)
    date_born = models.DateField('Fecha de nacimiento')
    height_born = models.FloatField('Altura al nacer')
    weight_born = models.FloatField('Peso al nacer')
    child_live = models.CharField('Con quién vive el menor', max_length=150)
    age_breastfeeding = models.IntegerField('Edad en que se abandona la lactancia materna', validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_born.year - ((today.month, today.day) < (self.date_born.month, self.date_born.day))


class ParentsChilds(BaseModel):
    '''
    Model's relation parents to child
    '''
    parent = models.ForeignKey(Parents, verbose_name='Adulto', on_delete=models.PROTECT)
    child = models.ForeignKey(Childs, verbose_name='Niño(a)', on_delete=models.PROTECT)
    relationship = models.ForeignKey(Relationship, verbose_name='Parentesco', on_delete=models.PROTECT)

    @property
    def parent_document(self):
        return self.parent.document


class ChildsDetail(BaseModel):
    '''
    Model's child (childs detail after consult)
    '''

    child = models.ForeignKey(Childs, verbose_name='Niño(a)', on_delete=models.PROTECT)
    height = models.FloatField('Altura', validators=[MinValueValidator(0),])
    weight = models.FloatField('Peso', validators=[MinValueValidator(0),])
    # type_diagnostic = models.ForeignKey(TypeDiagnostic, verbose_name='Tipo de Diagnostico', on_delete=models.PROTECT)

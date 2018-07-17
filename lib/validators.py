# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator


isalphanumericvalidator = RegexValidator(r'^[a-zA-Z0-9]*$',
                             message='Este campo debe ser alfanumérico.',
                             code='Inválido')

isnumbervalidator = RegexValidator(r'^[0-9]*$',
                             message='Este campo debe ser numérico.',
                             code='Inválido')

isalphavalidator = RegexValidator(r'^[a-zA-Z- ñÑ-áéíóúÁÉÍÓÚ]+$',
                             message='Este campo sólo permite letras.',
                             code='Inválido')
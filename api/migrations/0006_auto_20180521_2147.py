# Generated by Django 2.0.5 on 2018-05-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180521_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childs',
            name='document',
            field=models.CharField(error_messages={'unique': 'Est documento ya se encuentra registrado.'}, max_length=20, unique=True, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='document',
            field=models.CharField(error_messages={'unique': 'Est documento ya se encuentra registrado.'}, max_length=20, unique=True, verbose_name='Documento'),
        ),
    ]
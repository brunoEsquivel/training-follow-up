# Generated by Django 3.2.6 on 2021-11-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_alter_cuotausuario_fechainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuotausuario',
            name='fechaInicio',
            field=models.DateField(),
        ),
    ]

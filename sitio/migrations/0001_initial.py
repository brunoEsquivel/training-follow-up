# Generated by Django 3.2.7 on 2021-09-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('discord_user', models.CharField(max_length=100)),
                ('avatar_id', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HorasUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('lunes', models.IntegerField(default=-1)),
                ('martes', models.IntegerField(default=-1)),
                ('miercoles', models.IntegerField(default=-1)),
                ('jueves', models.IntegerField(default=-1)),
                ('viernes', models.IntegerField(default=-1)),
                ('sabado', models.IntegerField(default=-1)),
                ('promedio', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 2.0.6 on 2021-07-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_auto_20210709_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='autors',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='libros',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
    ]

# Generated by Django 2.0.6 on 2021-07-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20210709_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='autors',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
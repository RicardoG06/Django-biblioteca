# Generated by Django 2.0.6 on 2021-07-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_libros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='autor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Autors'),
        ),
    ]

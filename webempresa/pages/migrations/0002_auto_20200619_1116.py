# Generated by Django 2.1 on 2020-06-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.BigIntegerField(verbose_name='telefone'),
        ),
    ]

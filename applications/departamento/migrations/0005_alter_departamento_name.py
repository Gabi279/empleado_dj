# Generated by Django 4.0.5 on 2022-06-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0004_alter_departamento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]

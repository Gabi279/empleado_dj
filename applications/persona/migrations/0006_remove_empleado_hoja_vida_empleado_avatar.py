# Generated by Django 4.0.5 on 2022-06-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='hoja_vida',
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]

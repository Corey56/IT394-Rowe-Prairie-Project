# Generated by Django 2.1.5 on 2020-05-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMIApp', '0005_remove_cadets_cadet_has_superior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadets',
            name='X_Num',
            field=models.CharField(max_length=5),
        ),
    ]

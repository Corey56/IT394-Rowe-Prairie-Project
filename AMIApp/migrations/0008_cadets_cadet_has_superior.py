# Generated by Django 2.1.5 on 2020-05-08 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AMIApp', '0007_auto_20200504_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadets',
            name='cadet_has_superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='AMIApp.Cadet_Has_Superior'),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-08 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20211108_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='satellite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.satellite'),
        ),
        migrations.AddField(
            model_name='star',
            name='planet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.planet'),
        ),
    ]

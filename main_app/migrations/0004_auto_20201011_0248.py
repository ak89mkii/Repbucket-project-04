# Generated by Django 3.1.1 on 2020-10-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201011_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='leveling',
            field=models.CharField(choices=[('Active', 'Active'), ('Standby', 'Standby')], default='Active', max_length=20),
        ),
    ]

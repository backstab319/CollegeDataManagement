# Generated by Django 2.2.6 on 2019-10-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentData', '0002_auto_20191021_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=11),
        ),
    ]

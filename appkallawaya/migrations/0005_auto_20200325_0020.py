# Generated by Django 2.2.8 on 2020-03-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkallawaya', '0004_malestares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='cura',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.CharField(default='', max_length=1500),
        ),
    ]

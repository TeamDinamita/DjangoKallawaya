# Generated by Django 2.2.8 on 2020-03-27 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkallawaya', '0010_auto_20200326_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dolencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlantTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=1500)),
                ('cura', models.CharField(default='', max_length=1500)),
            ],
        ),
    ]
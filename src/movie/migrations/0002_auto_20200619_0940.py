# Generated by Django 3.0.7 on 2020-06-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='año',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]

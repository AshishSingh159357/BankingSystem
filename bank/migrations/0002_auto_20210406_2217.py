# Generated by Django 3.0.5 on 2021-04-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.IntegerField(),
        ),
    ]

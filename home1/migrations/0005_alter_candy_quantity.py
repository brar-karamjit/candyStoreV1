# Generated by Django 4.0.4 on 2022-05-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0004_candy_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candy',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0002_delete_candy'),
    ]

    operations = [
        migrations.CreateModel(
            name='candy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]

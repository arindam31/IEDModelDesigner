# Generated by Django 3.1.4 on 2020-12-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ied', '0014_auto_20201226_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logicalnode',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ied', '0011_auto_20201218_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribtype',
            old_name='desciption',
            new_name='description',
        ),
    ]

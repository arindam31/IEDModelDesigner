# Generated by Django 3.1.4 on 2020-12-26 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ied', '0012_auto_20201220_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logicalnode',
            name='logical_device',
        ),
        migrations.AddField(
            model_name='logicaldevice',
            name='logical_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ied.logicalnode'),
        ),
    ]

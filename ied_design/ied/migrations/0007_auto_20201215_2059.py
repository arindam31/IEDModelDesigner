# Generated by Django 3.1.4 on 2020-12-15 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ied', '0006_auto_20201215_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='data_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ied.dataobject'),
        ),
        migrations.AlterField(
            model_name='attribvalue',
            name='attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ied.attribute'),
        ),
        migrations.AlterField(
            model_name='dataobject',
            name='logical_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ied.logicalnode'),
        ),
        migrations.AlterField(
            model_name='logicaldevice',
            name='logical_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ied.ied'),
        ),
        migrations.AlterField(
            model_name='logicalnode',
            name='logical_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ied.logicaldevice'),
        ),
    ]

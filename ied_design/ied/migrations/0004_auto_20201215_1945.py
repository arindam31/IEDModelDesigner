# Generated by Django 3.1.4 on 2020-12-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ied', '0003_auto_20201215_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribtype',
            options={'verbose_name': 'AttibuteType', 'verbose_name_plural': 'AttriButeTypes'},
        ),
        migrations.AddField(
            model_name='attribute',
            name='attrib_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ied.attribtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='attrib_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ied.attribvalue'),
        ),
        migrations.AlterField(
            model_name='dataobject',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ied.attribute'),
        ),
        migrations.AlterField(
            model_name='logicaldevice',
            name='logical_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ied.logicalnode'),
        ),
        migrations.AlterField(
            model_name='logicalnode',
            name='data_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ied.dataobject'),
        ),
    ]
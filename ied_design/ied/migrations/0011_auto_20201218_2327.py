# Generated by Django 3.1.4 on 2020-12-18 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ied', '0010_attribute_attrib_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ied',
            options={'verbose_name': 'IED', 'verbose_name_plural': 'IEDs'},
        ),
        migrations.AddField(
            model_name='ied',
            name='manufacturer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

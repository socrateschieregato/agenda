# Generated by Django 2.0.2 on 2018-05-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telefones', '0002_auto_20180504_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefones',
            name='pessoa',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Pessoa'),
        ),
    ]

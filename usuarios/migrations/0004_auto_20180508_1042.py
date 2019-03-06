# Generated by Django 2.0.2 on 2018-05-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20180507_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='descricao',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cpf',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='CPF/CNPJ'),
        ),
    ]

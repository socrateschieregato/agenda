# Generated by Django 2.0.2 on 2018-05-04 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(default='', max_length=15, unique=True, verbose_name='Telefone')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_telefone', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='telefones',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telefones.Tipo_telefone'),
        ),
    ]

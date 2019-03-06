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
            name='Certificados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Compra')),
                ('validade', models.DateField()),
                ('password', models.CharField(default='', max_length=30)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Empresa')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.Tipo_status')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_certificado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_certificado', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='certificados',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.Tipo_certificado'),
        ),
    ]
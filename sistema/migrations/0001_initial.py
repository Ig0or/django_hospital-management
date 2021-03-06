# Generated by Django 4.0 on 2021-12-27 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField(max_length=5)),
                ('complemento', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField(max_length=11)),
                ('cpf', models.IntegerField(max_length=11)),
                ('profissao', models.CharField(max_length=30)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.endereco')),
            ],
        ),
    ]

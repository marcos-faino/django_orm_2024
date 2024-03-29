# Generated by Django 4.2.10 on 2024-02-08 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=150)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('NI', 'Não Informado')], max_length=13)),
                ('end_rua', models.CharField(max_length=50)),
                ('end_numero', models.IntegerField()),
                ('end_cep', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_realizacao', models.CharField(max_length=100)),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.aluno')),
            ],
            options={
                'verbose_name': 'Histórico',
                'verbose_name_plural': 'Históricos',
            },
        ),
    ]

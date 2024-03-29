# Generated by Django 4.2.10 on 2024-02-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cod_depto', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('num_alunos', models.PositiveSmallIntegerField()),
                ('curso', models.ManyToManyField(related_name='curso_disciplinas', to='core.curso')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-24 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_rename_exercicio1_treino_exercicio1_nome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treino',
            old_name='nome_aluno',
            new_name='aluno',
        ),
    ]

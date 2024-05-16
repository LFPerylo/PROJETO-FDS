# Generated by Django 5.0.4 on 2024-05-16 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_alter_progressoaluno_progresso_observado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_progresso', models.CharField(choices=[('forca', 'Força'), ('resistencia', 'Resistência'), ('circunferencia', 'Circunferência')], max_length=100)),
                ('data', models.DateField()),
                ('observacao', models.TextField()),
                ('nome_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.dados')),
            ],
        ),
        migrations.DeleteModel(
            name='ProgressoAluno',
        ),
    ]
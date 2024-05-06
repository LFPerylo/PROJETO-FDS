# Generated by Django 5.0.4 on 2024-05-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('administrador', 'Administrador'), ('usuario', 'Usuário')], default='usuario', max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]

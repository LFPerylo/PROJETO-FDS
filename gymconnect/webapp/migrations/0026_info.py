# Generated by Django 5.0.4 on 2024-05-27 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_metas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor_info', to='webapp.dados')),
            ],
        ),
    ]
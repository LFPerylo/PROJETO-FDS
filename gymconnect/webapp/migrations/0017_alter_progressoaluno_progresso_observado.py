# Generated by Django 5.0.4 on 2024-05-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_alter_progressoaluno_metrica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progressoaluno',
            name='progresso_observado',
            field=models.TextField(max_length=200),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guessedword',
            name='is_similar',
            field=models.CharField(blank=True, help_text='Процент совпадения с предполагаемым словом.', max_length=8, null=True, verbose_name='Схожесть'),
        ),
    ]

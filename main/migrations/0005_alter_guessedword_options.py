# Generated by Django 5.0.3 on 2024-04-09 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_room_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guessedword',
            options={'ordering': ['-created_at'], 'verbose_name': 'Предложенное слово', 'verbose_name_plural': 'Предложенные слова'},
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-07 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='odds',
            options={'verbose_name_plural': 'Odds'},
        ),
        migrations.RenameField(
            model_name='odds',
            old_name='draw',
            new_name='odd',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='w1',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='w2',
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadeira',
            name='projeto',
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Cadeira',
        ),
        migrations.DeleteModel(
            name='Projetos',
        ),
        migrations.DeleteModel(
            name='Utilizador',
        ),
    ]

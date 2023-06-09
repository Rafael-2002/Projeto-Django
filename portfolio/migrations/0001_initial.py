# Generated by Django 4.2.1 on 2023-06-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('data', models.DateField(auto_now_add=True)),
                ('conteudo', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=30)),
                ('comentario', models.CharField(max_length=100)),
            ],
        ),
    ]

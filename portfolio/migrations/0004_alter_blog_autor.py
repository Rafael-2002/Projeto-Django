# Generated by Django 4.2.1 on 2023-06-07 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_blog_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.utilizador'),
        ),
    ]
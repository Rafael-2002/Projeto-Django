# Generated by Django 4.2.1 on 2023-06-14 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0010_remove_blog_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=300)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.blog')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

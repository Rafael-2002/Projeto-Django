from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    ECTS = models.IntegerField()
    Ranking = models.IntegerField()

    def __str__(self):
        return self.nome


class Projetos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    tecnologias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Blog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
    conteudo = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Blog, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=300)


from django.db import models


class Perfil(models.Model):
    nome = models.CharField(max_length=200)
    dtNascimento = models.DateTimeField('Nascimento')


class Carro(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nomeCarro = models.CharField(max_length=200)
    corCarro = models.CharField(max_length=50)

from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    ]

    OBJETIVO_CHOICES = [
        ('perder-peso', 'Perder Peso'),
        ('manter-peso', 'Manter Peso'),
        ('ganhar-peso', 'Ganhar Massa Muscular'),
    ]

    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    idade = models.PositiveIntegerField()
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    altura_cm = models.PositiveIntegerField()
    nivel_atividade = models.DecimalField(max_digits=4, decimal_places=3) 
    objetivo = models.CharField(max_length=20, choices=OBJETIVO_CHOICES)
    faixa_renda = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return self.usuario.username

class Alimento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    custo_aproximado = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)
    calorias = models.PositiveIntegerField()
    proteinas = models.DecimalField(max_digits=5, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2)
    gorduras = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Cardapio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    alimentos = models.ManyToManyField(Alimento)
    calorias_totais = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Cardápio de {self.usuario.username} em {self.data_criacao}"
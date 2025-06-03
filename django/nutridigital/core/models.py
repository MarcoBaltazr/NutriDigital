from django.db import models

# Create your models here.
sexo_user = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

atv_fisica = [
    ('1', 'Sedentário'),
    ('2', 'Levemente ativo'),
    ('3', 'Moderadamente ativo'),
    ('4', 'Muito ativo'),
    ('5', 'Extremamente ativo'),
]

objetivo_user = [
    ('perda', 'Perder peso'),
    ('manter', 'Manter peso'),
    ('ganho', 'Ganho de massa muscular'),
]

renda_disp = [
    ('0-300', 'Até R$ 350,00'),
    ('350-800', 'Entre R$ 350,01 e R$ 800,00'),
    ('800-1500', 'Entre R$ 800,01 e R$ 1.500,00'),
    ('1500-3000', 'Entre R$ 1.500,01 e R$ 3.000,00'),
    ('3000+', 'Acima de R$ 3.000,01'),
]

class Questionario(models.Model):
    nome = models.CharField(max_length=50)
    sexo = models.CharField(choices=sexo_user)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    atv = models.CharField(choices=atv_fisica)
    objetivo = models.CharField(choices=objetivo_user)
    renda = models.CharField(choices=renda_disp)


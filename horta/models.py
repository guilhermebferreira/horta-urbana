# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Cliente(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    facebook_id = models.CharField( max_length=20, blank=False)
    nome = models.CharField( max_length=50, blank=False)
    endereco = models.CharField( max_length=100, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    quantidade_semana = models.IntegerField(default=1)
    pago_ate = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('nome',)


class Pacote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    organico = models.BooleanField(default=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    item_alface = models.BooleanField(default=True)
    item_tomate = models.BooleanField(default=True)
    item_cheiroverde = models.BooleanField(default=True)
    item_couve = models.BooleanField(default=True)

    class Meta:
        ordering = ('nome', 'organico',)

class Feirante(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField( max_length=50, blank=False)
    endereco = models.CharField( max_length=100, blank=False)
    organico = models.BooleanField(blank=True)
    cota_alface = models.IntegerField(default=0)
    cota_tomate = models.BooleanField(default=0)
    cota_cheiroverde = models.BooleanField(default=0)
    cota_couve = models.BooleanField(default=0)


    class Meta:
        ordering = ('nome', 'organico',)


ALFACE = 1
TOMATE = 2
CHEIROVERDE = 3
COUVE = 4

ITEM_CHOICES = (
    (ALFACE, "Alface"),
    (TOMATE, "Tomate"),
    (CHEIROVERDE, "Cheiro Verde"),
    (COUVE, "Couve"),
)

PENDENTE = 1
OK = 2

STATUS_CHOICES = (
    (PENDENTE, "Pendente"),
    (OK, "Ok"),
)

DIA_CHOICES = (
    (1, "Terça"),
    (2, "Quinta"),
)


class Pedido(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, blank=False)
    feirante = models.ForeignKey(Feirante, null=True, blank=True)
    organico = models.BooleanField(default=False)
    item = models.IntegerField(choices=ITEM_CHOICES, blank=False, default='1')
    status = models.IntegerField(choices=STATUS_CHOICES, blank=False, default='1')
    dia_semana = models.IntegerField(choices=DIA_CHOICES, blank=False, default='1')
    data = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('data', 'cliente',)



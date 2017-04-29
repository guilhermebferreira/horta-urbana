# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum


PENDENTE = 1
OK = 2

STATUS_CHOICES = (
    (PENDENTE, "Pendente"),
    (OK, "Ok"),
)

class Cliente(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    facebook_id = models.CharField( max_length=20, blank=False)
    nome = models.CharField( max_length=100, blank=False)
    endereco = models.CharField( max_length=500, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    quantidade_semana = models.IntegerField(default=1)
    pago_ate = models.DateField(null=True, blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)


    def __unicode__(self):
        return self.cliente.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'





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
        verbose_name = 'Pacote'
        verbose_name_plural = 'Pacote'

class Feirante(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField( max_length=50, blank=False)
    endereco = models.CharField( max_length=100, blank=False)
    organico = models.BooleanField(blank=True)
    cota_alface = models.IntegerField(default=0)
    cota_tomate = models.IntegerField(default=0)
    cota_cheiroverde = models.IntegerField(default=0)
    cota_couve = models.IntegerField(default=0)


    class Meta:
        ordering = ('nome', 'organico',)
        verbose_name = 'Feirante'
        verbose_name_plural = 'Feirantes'


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

    def cliente_nome(self):
        return self.cliente.nome


    def __unicode__(self):
        return u"%s - %s" % self.cliente.nome, self.item

    class Meta:
        ordering = ('data', 'cliente',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'



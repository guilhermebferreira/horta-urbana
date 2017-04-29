# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

DENGUE = 1
DENGUE_HEMO = 1

FOCO_CHOICES = (
    (DENGUE, "Dengue"),
    (DENGUE_HEMO, "Dengue hemorrágica"),
)

PALMAS = 1
PORTO = 2
PARAISO = 3

CIDADE_CHOICES = (
    (PALMAS, "Palmas"),
    (PORTO, "Porto Nacional"),
    (PARAISO, "Paraíso do Tocantins"),
)


class Foco(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.IntegerField(choices=FOCO_CHOICES, blank=False, default='1')
    city = models.IntegerField(choices=CIDADE_CHOICES, blank=False, default='1')

    class Meta:
        ordering = ('created','city',)

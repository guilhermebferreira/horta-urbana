# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


#gerar saida para heatmap https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap

from rest_framework.viewsets import (
    ModelViewSet,
)
from .models import Foco
from .serializers import FocoSerializer


class FocoViewSet(ModelViewSet):

    queryset = Foco.objects.all()
    serializer_class = FocoSerializer

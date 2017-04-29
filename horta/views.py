import json
from collections import namedtuple

from django.core import serializers
from django.shortcuts import render
import datetime
from django.utils import formats
from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import (
    ModelViewSet,
)

from .models import Pedido, Feirante, Pacote, Cliente, ITEM_CHOICES
from .serializers import PedidoSerializer, FeiranteSerializer, PacoteSerializer, ClienteSerializer

class PedidoViewSet(ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PacoteViewSet(ModelViewSet):

    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer


class FeiranteViewSet(ModelViewSet):
    queryset = Feirante.objects.all()
    serializer_class = FeiranteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


@api_view(('POST',))
def criar_pedido(request):
    # {
    #     "periodicidade": "2",
    #     "address": "Faculdade Católica do Tocantins, Avenida Teotônio Segurado, 1402 Sul (ACSU-SE 140), Condomínio Mirante do Lago (ALC-SO 141), Palmas, Microrregião de Porto Nacional, Mesorregião Oriental do Tocantins, Tocantins, North Region, Brazil",
    #     "chatfuel user id": "1402991029758221",
    #     "city": "Palmas",
    #     "first name": "Luiz",
    #     "latitude": "-10.270254135131836",
    #     "map url": "https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.bing.com%2Fmaps%2Fdefault.aspx%3Fv%3D2%26pc%3DFACEBK%26mid%3D8100%26where1%3D-10.2702537%252C%2B-48.3320384%26FORM%3DFBKPL1%26mkt%3Den-US&h=ATMhmUFHqEb4yN3JosCxw-Qxb4xASlpQgcae2gZupcaom40ZxKI74o5O5lq_JNR4KiNfvM-21WIiRzcskJLIFv_rnbaYesTv_LK8KPbXQOnS&s=1&enc=AZOJQrY38lDd51jhhMlV7Owz2iVtitMUdcsvnfEmlCtpONdR-3knaxdfJuNJWtfrk3j_kjlKzE7uQ9NfXplgTZ0e",
    #     "messenger user id": "1402991029758221",
    #     "complemento": "RUa 01, fim da rua",
    #     "meses": "3"
    # }
    #entregas todas as terças e quintas
    try:
        #select do cliente pelo facebook idtry:
        p_cliente = Cliente.objects.get(facebook_id=request.data['messenger user id'])
    except Cliente.DoesNotExist:
        #criar cliente
        p_cliente = Cliente(
            facebook_id=request.data['messenger user id'],
            nome=request.data['first name'],
            endereco=request.data['address'],
            latitude=request.data['latitude'],
            longitude=request.data['latitude'],
            quantidade_semana=request.data['periodicidade']

        )
        p_cliente.save()


    try:
        p_pacote = Pacote.objects.get(id=request.data['pacote'])
        valor = float(0)
        today = datetime.date.today()
        terca = today + datetime.timedelta((1 - today.weekday()) % 7)
        quinta = today + datetime.timedelta((3 - today.weekday()) % 7)
        for i in range(int(request.data['meses'])):
            for d in range(4):
                for choice_id, choice_label in ITEM_CHOICES:
                    novo_pedido = Pedido(
                        cliente=p_cliente,
                        organico=p_pacote.organico,
                        item=choice_id,
                        dia_semana=1,
                        data=terca
                    )
                    novo_pedido.save()
                valor += float(p_pacote.preco)

                if request.data['periodicidade'] == '2':
                    for choice_id, choice_label in ITEM_CHOICES:
                        novo_pedido = Pedido(
                            cliente=p_cliente,
                            organico=p_pacote.organico,
                            item=choice_id,
                            dia_semana=2,
                            data=quinta
                        )
                        novo_pedido.save()
                    valor += float(p_pacote.preco)
                    terca += datetime.timedelta(days=7)
                    quinta += datetime.timedelta(days=7)
        p_cliente.preco = valor
        p_cliente.save()

    except Exception as e:
        return Response(
            {
                "message":  str(e),
                "request" : request.data,
                "cliente" : p_cliente.nome,
                "teste" : request.data['chatfuel user id']
            })

    return Response({
              "messages": [
                {
                  "attachment": {
                    "type": "template",
                    "payload": {
                      "template_type": "button",
                      "text": "Obrigado por requisitar sua assinatura.\nPara finalizar, transfira o valor de R$ "+str(valor)+" para:\nBanco do Brasil\nConta corrente: xxxx-x\nConta Poupança: xxxxxx-x\nNOME DO CORRENTISTA",
                      "buttons": [
                        {
                          "type": "show_block",
                          "block_name": "COMPROVANTE",
                          "title": "Enviar comprovante"
                        }
                      ]
                    }
                  }
                }
              ]
            })


@api_view(('GET',))
def pedidos_cliente(request, format=None):
    return Response({
        'clientes': reverse('cliente-list', request=request, format=format),
        'feirantes': reverse('feirante-list', request=request, format=format)
    })


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'clientes': reverse('cliente-list', request=request, format=format),
        'feirantes': reverse('feirante-list', request=request, format=format)
    })

@api_view(('GET',))
def quantidade(request):
    response = {}
    for choice_id, choice_label in ITEM_CHOICES:
        o_pedido = Pedido.objects.filter(item=choice_id).filter(status=2)
        m_quantidade = len(o_pedido)
        response[choice_label] = str(m_quantidade)

    return JsonResponse(response)


@api_view(('GET',))
def assinatura_status(request):
    response = {}
    try:
        pass
        #select do cliente pelo facebook idtry:
        #p_cliente = Cliente.objects.get(facebook_id=request.data['messenger user id'])
    except Cliente.DoesNotExist:
        pass
        #response['periodicidade'] = "0"
        #response['quantidade'] = "0"
        #response['endereco'] = " teste "

    #response['periodicidade'] = str(p_cliente.quantidade_semana)

    #p_quantidade = Pedido.objects.filter(cliente=p_cliente).values('data').order_by('data')

    #m_quantidade = len(p_quantidade)
    #response['quantidade'] = str(m_quantidade)

    return Response({"messages":[{"text":"🕐 Periodicidade: 2 vezes por semana \n📌 Endereço atual: 1402 Sul (ACSU-SE 140) \n📆 Quantidade de semanas a receber: 24"}]})



def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())


def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


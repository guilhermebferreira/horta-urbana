from rest_framework.serializers import (
    ModelSerializer,
)
from .models import Pedido, Feirante, Pacote, Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'facebook_id', 'latitude', 'longitude', 'endereco', 'quantidade_semana', 'pago_ate')


class PacoteSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = ('nome', 'descricao', 'organico', 'preco')


class FeiranteSerializer(ModelSerializer):
    class Meta:
        model = Feirante
        fields = ('nome', 'endereco', 'organico', 'cota_alface', 'cota_tomate', 'cota_cheiroverde', 'cota_couve')


class PedidoSerializer(ModelSerializer):

    class Meta:
        model = Pedido
        fields = ('created', 'nome', 'endereco', 'pago_ate')

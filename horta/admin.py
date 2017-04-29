from django.contrib import admin

from .models import Pedido, Feirante, Pacote, Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'endereco')


class FeiranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'organico', 'endereco')


class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'organico')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'item', 'data')
    list_filter = (
        ('cliente', admin.RelatedOnlyFieldListFilter),
    )

admin.site.register(Feirante, FeiranteAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Pacote, PacoteAdmin)
# Register your models here.
#admin.site.register(Pedido)
#admin.site.register(Feirante)
#admin.site.register(Pacote)

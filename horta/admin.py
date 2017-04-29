from django.contrib import admin

from .models import Pedido, Feirante, Pacote, Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(Cliente, ClienteAdmin)
# Register your models here.
admin.site.register(Pedido)
admin.site.register(Feirante)
admin.site.register(Pacote)

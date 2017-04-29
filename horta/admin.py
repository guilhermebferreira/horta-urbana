from django.contrib import admin

from .models import Pedido, Feirante, Pacote, Cliente

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Feirante)
admin.site.register(Pacote)
admin.site.register(Cliente)

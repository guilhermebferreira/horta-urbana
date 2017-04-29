from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

# from myapp import views as views_books
# from foco import views as views_foco

#router = routers.DefaultRouter()
# router.register(r'books', views_books.BookViewSet)
# router.register(r'foco', views_foco.FocoSerializer)
from rest_framework.urlpatterns import format_suffix_patterns

from horta.views import PedidoViewSet, PacoteViewSet, FeiranteViewSet, ClienteViewSet, api_root, criar_pedido, pedidos_cliente
from rest_framework import renderers

pedido_list = PedidoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

pacote_list = PacoteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

feirante_list = FeiranteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

cliente_list = ClienteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

cliente_detail = ClienteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})

feirante_detail = FeiranteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^pedidos/$', pedido_list, name='pedido-list'),
    url(r'^clientes/$', cliente_list, name='cliente-list'),
    url(r'^pacotes/$', pacote_list, name='cliente-list'),
    url(r'^feirantes/$', feirante_list, name='feirante-list'),
    url(r'^pedir/$', criar_pedido, name='criar-pedido'),
    url(r'^clientes/(?P<pk>[0-9]+)/$', cliente_detail, name='cliente-detail'),
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^feirantes/(?P<pk>[0-9]+)/$', feirante_detail, name='feirante-detail')
])




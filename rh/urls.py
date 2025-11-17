from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('produtos/produtos',views.produtos, name='produtos'),
    path('clientes/',views.clientes, name='clientes'),
    path('funcionarios/',views.funcionarios, name='funcionarios'),
    path('accounts/register/', views.registro_usuario_view, name='register'),
    path('contato/contatos', views.formulario_contato_view, name='contatos'),
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
]


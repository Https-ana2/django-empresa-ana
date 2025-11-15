from django.contrib import admin
from .models import Funcionarios, Contato, Clientes, Produtos

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    # Quais colunas mostrar na lista de produtos
    list_display = ('nome', 'cargo', 'departamento', 'data_contratacao','status')
    # Por quais campos podemos buscar
    search_fields = ("nome",)
    # Quais campos podemos filtrar
    list_filter = ('status', 'data_contratacao')
    
# admin.site.register(Funcionarios)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade' , 'email', 'contato')
    list_filter = ('nome', 'idade' , 'email', 'contato')
    search_fields = ('nome','idade', 'email', 'contato')

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria' , 'descricao', 'valor')
    list_filter = ('nome', 'categoria' , 'descricao', 'valor')
    search_fields = ('nome', 'categoria' , 'descricao', 'valor')
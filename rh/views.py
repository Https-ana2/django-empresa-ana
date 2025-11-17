from django.shortcuts import redirect, render
# Importa Clientes para correção do bug e o decorador de autenticação
from .models import Funcionarios, Produtos, Clientes 
from .forms import ContatoModelForm
from django.contrib.auth.decorators import login_required

# Aplica o decorador para proteger a view
@login_required
def home(request):
    return render(request,'home.html')

# Aplica o decorador para proteger a view
@login_required
def produtos(request):
    produtos = Produtos.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request,'produtos.html', context)
    
# Aplica o decorador para proteger a view
@login_required
def clientes(request):
    # CORREÇÃO: Busca todos os clientes para exibir no template
    clientes = Clientes.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request,'clientes.html', context)

# Aplica o decorador para proteger a view
@login_required
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)

# A view principal do formulário (Não requer login)
def formulario_contato_view(request):

    if request.method == 'POST':
        # Cria a instância do formulário com os dados vindos do request
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            # A MÁGICA DO MODELFORM:
            # form.save() cria e salva um novo objeto 'MensagemContato'
            # no banco de dados com os dados do formulário.
            form.save()
            
            # Redireciona para uma página de sucesso
            return redirect('contato_sucesso')
    
    else:
        # Se for um GET, apenas cria um formulário vazio
        form = ContatoModelForm()

    # Passa o formulário (vazio ou com erros) para o template
    return render(request, 'contato/contatos.html', {'form': form})


# Uma view simples para a página de "sucesso" (Não requer login)
def contato_sucesso_view(request):

    return render(request, 'contato/contato_sucesso.html')

# As views incompletas formulario_cliente_view, cliente_cadastro_view e formulario_produtos_view foram removidas para limpeza.
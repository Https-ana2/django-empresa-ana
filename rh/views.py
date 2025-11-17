from django.shortcuts import redirect, render
from .models import Funcionarios, Produtos, Clientes 
from .forms import ContatoModelForm, CustomUserCreationForm 
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def produtos(request):
    produtos = Produtos.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request,'produtos.html', context)

@login_required
def clientes(request):
    clientes = Clientes.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request,'clientes.html', context)

@login_required
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)

def registro_usuario_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login') 
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})

def formulario_contato_view(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect('contato_sucesso')
    
    else:
        form = ContatoModelForm()

    return render(request, 'contato/contatos.html', {'form': form})

def contato_sucesso_view(request):

    return render(request, 'contato/contato_sucesso.html')

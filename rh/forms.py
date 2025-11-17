from django import forms
from .models import Contato
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass

class ContatoModelForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        
        fields = ['nome', 'email','celular', 'assunto', 'descricao']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'placeholder': '12 34567-8910', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto da mensagem', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem...', 'class': 'form-control'}),
        }
        
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
            'celular': 'Seu celular',
        }
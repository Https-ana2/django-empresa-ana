from django.db import models
from django.db import models
from django.utils import timezone


# Create your models here.
class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    #corrige o problema de duplo 's' no nome do modelo no admin
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" # Define o nome plural correto
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(max_length=150)
    assunto = models.CharField(max_length=200)
    descricao = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['-data_envio']

class Clientes(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes" # Define o nome plural correto
    def __str__(self):
        return self.nome

class Produtos(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos" # Define o nome plural correto
    def __str__(self):
        return self.nome

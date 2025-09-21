# Em core/admin.py

from django.contrib import admin
from .models import Pessoa, Endereco

# Esta classe permite cadastrar endereços diretamente na página da pessoa
class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1 # Mostra 1 formulário de endereço em branco por padrão

# Registra o modelo Pessoa no admin
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario')
    inlines = [EnderecoInline] # Adiciona a edição de endereços na página de Pessoa
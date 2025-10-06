from django.contrib import admin
from .models import Pessoa, Endereco

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Endereco)
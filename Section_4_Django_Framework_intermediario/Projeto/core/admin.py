from django.contrib import admin

from .models import Produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'slug', 'criado', 'modificado', 'ativo')

"""
@admin.register(Produto) ou
admin.site.register(Produto, ProdutoAdmin)
"""
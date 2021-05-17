from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', '_author')
    exclude = ('author')

    def _author(self, instance):
        return f'{instance.author.get_full_name()}'

    """
    Apresenta os dados somente do author que está logado
    Ele está sobreescrevendo o método da superclasse
    """
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(author=request.user)
    """
    Como fora excluído a apresentação do campo author pelo
    exclude('author'), ao salvar ele apresenta erro, pois
    para salvar o post precisa do author.
    Para isso, podemos modificar o método save_model, que é o
    método da superclasse para salvar o modelo.
    A modificação é salvar no objeto o nome do usuário.
    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    
    
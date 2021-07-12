# Precisa gerar PDF na sua aplicação Django? Vamos lá!

Criar um novo projeto e ambiente virtual e instalar:

```bash
pip install django 

pip install reportlab

pip freeze > requirements.txt

django-admin startproject relatorio

django-admin startapp core
```

Depois fazer as configurações no Section_12_Bonus\Aula_1_charts\charts\charts\settings.py:

```python
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap4',
    'chartjs',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

Criar rotas Section_12_Bonus\Aula_2_relatorio_pdf\relatorio\core\urls.py:

```python
from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

```

Section_12_Bonus\Aula_2_relatorio_pdf\relatorio\relatorio\urls.py:

```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
```

Criar views: Section_12_Bonus\Aula_2_relatorio_pdf\relatorio\core\views.py:

```python
import io
from django.http import FileResponse
from django.views.generic import  View

from reportlab.pdfgen import canvas

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        
        #cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()
        
        #Cria o arquivo pdf
        pdf = canvas.Canvas(buffer)
        
        # Insere coisas no pdf
        pdf.drawString(250, 500, 'Geek University')
        
        #Quando acabamos de inserrir coisas no pdf
        pdf.showPage()
        pdf.save()
        
        # por fim, retornamos o buffer para o inicio do arquivo
        buffer.seek(0)
        
        # Faz download do arquivo em PDF gerado
        #return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')
        
        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')

```

Outra biblioteca interessante: [weasyprint](https://weasyprint.org/), porém é interessante
que se faça a instalação no linux devido a suas dependecias.

Instalar o weasyprint:
```python

pip install weasyprint

```


Criar uma pagina html Section_12_Bonus\Aula_2_relatorio_pdf\relatorio\core\templates\relatorio.html:

```html
<html>
    <head>
        <title>Geek Report</title>
        <style>
            body{
                background: #0080ff;
            }
        </style>
    </head>
    <body>
        <h1>Geek Report</h1>
        {% for paragrafo in texto %}
            <p>{{ paragrafo }}</p>
        {% endfor %}
    </body>
</html>

```

Em views: Section_12_Bonus\Aula_2_relatorio_pdf\relatorio\core\views.py:

```python
import io
from django.http import FileResponse
from django.views.generic import  View

from reportlab.pdfgen import canvas

### weasyprint ###

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
### weasyprint ###

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        
        #cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()
        
        #Cria o arquivo pdf
        pdf = canvas.Canvas(buffer)
        
        # Insere coisas no pdf
        pdf.drawString(250, 500, 'Geek University')
        
        #Quando acabamos de inserrir coisas no pdf
        pdf.showPage()
        pdf.save()
        
        # por fim, retornamos o buffer para o inicio do arquivo
        buffer.seek(0)
        
        # Faz download do arquivo em PDF gerado
        #return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')
        
        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')


### weasyprint ###

class Index2View(View):
    def get(self, request, *args, **kwargs):
        texto =['Geek University', 'Evolua seu lado Geek', 'Programação em Django']
        
        html_string = render_to_string('relatorio.html', {texto: texto})
        
        html = HTML(string=html_string)
        
        html.write.pdf(target='/tmp/relatorio2.pdf')
        
        fs = FileSystemStorage('/tmp')
        
        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # Faz o download do arquivo PDF
            # response['Content-Disposition'] = 'attachment'; filename="relatorio2.pdf"'
            # Abri o PDF direto no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response
        

```

Em Section_12_Bonus\Aula_2_relatorio_pdf\relatorio\core\urls.py:

```python
from django.urls import path

from .views import IndexView, Index2View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('2/', Index2View.as_view(), name='index2'),
]


```


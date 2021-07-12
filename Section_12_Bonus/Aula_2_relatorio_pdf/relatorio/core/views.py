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
        
        
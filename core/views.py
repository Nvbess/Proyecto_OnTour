from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from io import BytesIO
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template,render_to_string 

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def contrato(request):
    if request.method == 'POST':
        formulario = ContratoCreation(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Contrato creado correctamente!")
            return redirect('contrato')  # Redirige a la misma vista después de guardar
        else:
            messages.error(request, "No se pudo generar el contrato!")
    else:
        formulario = ContratoCreation()

    aux = {'form': formulario}
    return render(request, 'core/contrato.html', aux)

def listarContrato(request):
    contratos = Contrato.objects.all()

    aux = {'contratos': contratos}
    return render(request, 'core/listar-contrato.html', aux)

def verContrato(request, id):
    contratos = get_object_or_404(Contrato, id=id)

    return render(request, 'core/ver-contrato.html', {'x': contratos})

def contrato_to_pdf(request, id):
    contratos = get_object_or_404(Contrato, id=id)
    
    html = render_to_string('core/contrato-pdf.html', {'x': contratos})
    
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="voucher_{contratos.id}.pdf"'
        return response
    
    return HttpResponse('Error al generar el PDF.', status=500)
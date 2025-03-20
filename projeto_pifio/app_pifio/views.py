from django.shortcuts import render
from .models import Pifios
def home(request):
    return render(request, 'usuarios/home.html')
def criar_pifio(request):
    if request.method == 'POST':
        novo_pifio = Pifios()
        novo_pifio.nome = request.POST.get('Pifio')
        novo_pifio.save()
        
    return render(request, 'usuarios/pifios.html')

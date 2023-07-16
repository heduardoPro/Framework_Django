from django.shortcuts import render
from .models import Arquivo

def home(request):
    
    context = {
        'text': 'Olá Home'
    }

    return render(
        request,
        'home/index.html',
        context,
    )

def upload_arquivo(request):
    
    if request.method == 'POST':
        arquivo = request.FILES['arquivo']
        novo_arquivo = Arquivo(arquivo=arquivo)
        novo_arquivo.save()
        return render(request, 'upload_success.html')
    else:
        return render(request, 'upload_form.html')

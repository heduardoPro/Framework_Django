from django.shortcuts import render

def home(request):
    
    context = {
        'text': 'Olá Home'
    }

    return render(
        request,
        'home/index.html',
        context,
    )
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
    else:
        form = ImageForm()

        images = Image.objects.all()

        context = {
        'form': form,
        'images': images
        }

        return render(request, 'home/index.html', context)

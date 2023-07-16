from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def home(request):
    uploaded = False

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uploaded = True
            return redirect('home:home')
    else:
        form = ImageForm()

        images = Image.objects.all()

    context = {
    'form': form,
    'images': images,
    'uploaded': uploaded,
    }

    return render(request, 'home/index.html', context)
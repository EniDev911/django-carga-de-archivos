from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagen
from .forms import ImagenForm
# Create your views here.
def index(request):

    if request.method == "POST":
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImagenForm()
    return render(request, 'index.html', {'form': form, 'images': Imagen.objects.all()})

def eliminar_imagen(request, id):
    imagen = get_object_or_404(Imagen, id=id)
    imagen.delete()
    return redirect('index')
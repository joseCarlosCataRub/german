from django.shortcuts import render
from .models import Equipos

# Create your views here.
def principal(request):
    return render(request, 'furbo/principal.html')

def equipos(request):
    context = Equipos.objects.all()
    return render(request, 'furbo/equipos.html', {'equipos': context})
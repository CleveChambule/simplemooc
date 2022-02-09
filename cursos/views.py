from django.shortcuts import render
from .models import Curso

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos' : cursos
    }
    return render(request, 'courses/index.html', context)
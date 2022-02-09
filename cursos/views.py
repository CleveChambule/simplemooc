from django.shortcuts import render
from .models import Curso

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos' : cursos
    }
    return render(request, 'courses/index.html', context)

def details(request, pk):
    curso = Curso.objects.get(pk=pk)
    context = {
        'curso': curso
    }
    return render(request, 'courses/details.html', context)

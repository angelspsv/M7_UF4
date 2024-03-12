from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    students = "Student.objects.all()"
    return render(request, 'alumnat.html', {'students': students})

def student(request, pk):
    students = {"nom": "Angel", "cognom": "Ivanov", "edat": "16", "rol": "alumne(TOP)", "curs": "DAW+"}
    return render(request, 'alumne.html', {'alumne': students})

def teachers(request):
    teachers = "Teacher.objects.all()"
    return render(request, 'professorat.html', {'teachers': teachers})

def teacher(request, pk):
    professor = {"nom": "Roger", "cognom": "Sobrino", "edat": "17", "rol": "teacher", "curs": "DAW8"}
    return render(request, 'professor.html', {'professor': professor})
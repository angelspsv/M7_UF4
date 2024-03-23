from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .forms import PersonForm


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    students = "Student.objects.all()"
    return render(request, 'alumnat.html', {'students': students})

def student(request, pk):
    students = [
        {"nom": "Angel", "cognom": "Ivanov", "edat": "38", "rol": "alumne", "curs": "DAW1, DAW2A"},
        {"nom": "Ramon", "cognom": "Garcia", "edat": "25", "rol": "alumne", "curs": "DAW2A"},
        {"nom": "Laura", "cognom": "Fernandez", "edat": "24", "rol": "alumne", "curs": "DAW2A"}
    ]
    student = students[int(pk)-1]
    return render(request, 'alumne.html', {'alumne': student})

def teachers(request):
    teachers = "Teacher.objects.all()"
    return render(request, 'professorat.html', {'teachers': teachers})

def teacher(request, pk):
    teachers = [
        {"nom": "Roger", "cognom": "Sobrino", "edat": "39", "rol": "teacher", "curs": "DAM2B, DAW2A"},
        {"nom": "Pere", "cognom": "Guitart", "edat": "57", "rol": "teacher", "curs": "DAW1"},
        {"nom": "Juanma", "cognom": "Biel", "edat": "50", "rol": "teacher", "curs": "DAW2B, DAW2A"}
    ]
    teacher = teachers[int(pk)-1]
    return render(request, 'professor.html', {'professor': teacher})

def form(request):
    form = PersonForm()
    context = {'form':form}
    return render(request, 'new_user_form.html', context)

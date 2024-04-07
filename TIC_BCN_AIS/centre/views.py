from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from.forms import PersonForm
from .models import Persona


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def students(request):
    students = Persona.objects.filter(rol='alumne')
    context = {'students': students}
    return render(request, 'alumnat.html', context)


def student(request, pk):
    student = Persona.objects.get(id = pk)
    return render(request, 'alumne.html', {'alumne': student})

def teachers(request):
    teachers = Persona.objects.filter(rol='professor')
    context = {'teachers': teachers}
    return render(request, 'professorat.html', context)


def teacher(request, pk):
    teacher = Persona.objects.get(id=pk)
    return render(request, 'professor.html', {'professor': teacher})

def form(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request, 'new_user_form.html', context)


def display_data(request):
    personas = Persona.objects.all().order_by('id')
    context = {'personas': personas}
    return render(request, 'display.html', context)


def update_user(request, pk):
    person = Persona.objects.get(id = pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'update_user_form.html', context)

def delete_user(request, pk):


    person = Persona.objects.get(id=pk)

    if request.method == 'POST':
        person.delete()
        return redirect('index')

    context = {'object':person}
    return render(request, 'delete_user.html', context)
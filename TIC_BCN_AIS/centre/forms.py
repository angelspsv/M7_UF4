from django.forms import ModelForm
from .models import Persona

class PersonForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
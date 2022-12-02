
from django.forms import ModelForm
from django import forms
from .models import login,registro,registroVuelo

class loginFormulario(forms.Form):
    usuario = forms.CharField(max_length=100,min_length=5,label='Usuario')
    password = forms.CharField(min_length=5,max_length=10,label='Contraseña'
        ,widget=forms.PasswordInput)

class registroFormulario(ModelForm):
    class Meta:
        model = registro
        fields = ['nombre','apellido','correo','usuario','password','password2']
        #contraseña encriptada
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        #cambial nombre de campos
        }
        labels = {
            'password': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }


class registroVueloFormulario(ModelForm):
    class Meta:
        model = registroVuelo
        fields = ['matricula','fecha','piloto','instructor','etapaCurso','vueloSolo','origen','destino','horometro_ini','horometro_fin','tacometro_ini','tacometro_fin','combus_ini','combus_fin','observacion']
        
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

from django.forms import *

class NombreApellidoEmailForm(Form):
    nombre=CharField(max_length=20,label='Introduce tu nombre',help_text='Tu nombre No debe contener: Numeros, simbolos')
    apellido=CharField(max_length=20,label='Introduce tu apellido',help_text='Tu apellido No debe contener: Numeros, simbolos')
    email=EmailField(max_length=40,label='Introduce tu email',help_text='Tu direccion email: Midireccion@ejemplo.com')
    cedula=IntegerField(min_value=20000000,max_value=26000000,label='Introduce tu cedula', help_text='Tu cedula de identidad, sin comas, ni puntos')

class ComentarioForm(Form):
    comentario=CharField(widget=Textarea(attrs={'style':'width:600px; height:60px;','id':'comentario'}))

class ImagenForm(Form):
    imagen=ImageField(label='Tu imagen')

class ArchivoForm(Form):
    archivo=FileField(label='Tu planilla de notas')
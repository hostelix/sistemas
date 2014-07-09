from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cedulas(models.Model):
    cedula_user=models.IntegerField(unique=True)

    def __str__(self):
        return "%s"%self.cedula_user

class Usuarios(models.Model):
    cedula=models.ForeignKey(Cedulas,unique=True)
    usuario=models.ForeignKey(User)
    imagen=models.ImageField(blank=True,upload_to='imagen', verbose_name='Imagen')
    visitas=models.SmallIntegerField(default=0)


class Comentarios(models.Model):
    comentario=models.TextField(max_length=250)
    usuario=models.ForeignKey(User)
    imagen=models.ForeignKey(Usuarios)
    fecha=models.DateField(auto_now=True)
    hora=models.TimeField(auto_now=True)

    def __str__(self):
        return "%d [%s]"%self.usuario,self.comentario

class Notas(models.Model):
    cedula=models.ForeignKey(Cedulas)
    codigo=models.CharField(max_length=25)
    leyenda=models.ForeignKey('Leyenda')
    ver=models.BooleanField(default=1)
    nota1=models.CharField(blank=True,default=0,max_length=15)
    nota2=models.CharField(blank=True,default=0,max_length=15)
    nota3=models.CharField(blank=True,default=0,max_length=15)
    nota4=models.CharField(blank=True,default=0,max_length=15)
    nota5=models.CharField(blank=True,default=0,max_length=15)
    nota6=models.CharField(blank=True,default=0,max_length=15)
    nota7=models.CharField(blank=True,default=0,max_length=15)
    nota8=models.CharField(blank=True,default=0,max_length=15)
    nota9=models.CharField(blank=True,default=0,max_length=15)
    nota10=models.CharField(blank=True,default=0,max_length=15)
    nota11=models.CharField(blank=True,default=0,max_length=15)
    nota12=models.CharField(blank=True,default=0,max_length=15)
    notaDef=models.CharField(blank=True,default=0,max_length=15)


class Leyenda(models.Model):
    codigo=models.CharField(max_length=25)
    leyenda1=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda2=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda3=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda4=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda5=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda6=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda7=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda8=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda9=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda10=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda11=models.CharField(blank=True,default='Nota',max_length=20)
    leyenda12=models.CharField(blank=True,default='Nota',max_length=20)
    leyendaDef=models.CharField(blank=True,default='Nota',max_length=20)

class Planillas(models.Model):
    archivo=models.FileField(upload_to='carga',blank=False,verbose_name='Planilla',)
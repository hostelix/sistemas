# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from pagina.models import *
from pagina.mensajes import *
from pagina.formulario import *
from pagina.ver_planilla import AddNotas
import os

####################Funciones#######################
def permitir_extension(nombredelarchivo):
    extension=str(nombredelarchivo)
    extension=extension.split('.')
    if extension:
        for n in extension:
            if str(n) =='xls':
                return True
        return False
    else:
        return False

def agregar_nom_ape(usuario,nombre,apellido,email):
    consulta=User.objects.get(username=usuario)
    consulta.first_name=nombre
    consulta.last_name=apellido
    consulta.email=email
    consulta.save()

def agreagar_cedula_user(usuario,cedula):
    user=User.objects.get(username=usuario)
    cedula=Cedulas.objects.get(cedula_user=cedula)
    com=Usuarios.objects.create(usuario=user,cedula=cedula)
    com.save()

def agregar_leyenda(lista_leyenda,modelo,materia):
    model=modelo.objects.filter(codigo=materia)
    if model:
        model.update(leyenda1=lista_leyenda[0],leyenda2=lista_leyenda[1],
                                     leyenda3=lista_leyenda[2],leyenda4=lista_leyenda[3],leyenda5=lista_leyenda[4],
                                     leyenda6=lista_leyenda[5],leyenda7=lista_leyenda[6],leyenda8=lista_leyenda[7],
                                     leyenda9=lista_leyenda[8],leyenda10=lista_leyenda[9],leyenda11=lista_leyenda[10],
                                     leyenda12=lista_leyenda[11],leyendaDef=lista_leyenda[12])

    else:
        indice=modelo.objects.create(codigo=materia,leyenda1=lista_leyenda[0],leyenda2=lista_leyenda[1],
                                     leyenda3=lista_leyenda[2],leyenda4=lista_leyenda[3],leyenda5=lista_leyenda[4],
                                     leyenda6=lista_leyenda[5],leyenda7=lista_leyenda[6],leyenda8=lista_leyenda[7],
                                     leyenda9=lista_leyenda[8],leyenda10=lista_leyenda[9],leyenda11=lista_leyenda[10],
                                     leyenda12=lista_leyenda[11],leyendaDef=lista_leyenda[12])
        indice.save()


def existe_cedula_registrada(consulta):
    try:
        Usuarios.objects.get(cedula=consulta.pk)
        return False
    except:
        return True

def agregar_visita(usuario):
    user=User.objects.get(username=usuario)
    visita=Usuarios.objects.get(usuario=user.pk)
    visita.visitas=visita.visitas+1
    visita.save()

def agregar_comentario(request,modelo,dato):
    add=modelo.objects.create(
        comentario=request.POST['comentario'],
        usuario=request.user,
        imagen=dato)
    add.save()



####################################################
def inicio(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def registro(request):
    mensaje=()
    if request.method == 'POST':
        nuevoregistro=UserCreationForm(request.POST)
        add_nom_ape=NombreApellidoEmailForm(request.POST)
        if nuevoregistro.is_valid() and add_nom_ape.is_valid():
            cedula=request.POST['cedula']
            existe=Cedulas.objects.get(cedula_user=cedula)
            if existe:
                if existe_cedula_registrada(existe):
                    nuevoregistro.save()
                    #Agregamos nombre, apellido, email al usuario
                    agregar_nom_ape(request.POST['username'],request.POST['nombre'],request.POST['apellido'],request.POST['email'])
                    #Agregamos los FK de kda usuario para familiarizarlos con las cedulas
                    agreagar_cedula_user(request.POST['username'],cedula)
                    nuevoregistro=UserCreationForm()#Mostramos los formulario vacios
                    add_nom_ape=NombreApellidoEmailForm()#Mostramos los formulario vacios
                    mensaje=mensajes_listo
                else:
                    mensaje=mensajes_db_existe
            else:
                mensaje=mensajes_db
        else:
            mensaje=mensajes_formulario_campo
    else:
        nuevoregistro=UserCreationForm()
        add_nom_ape=NombreApellidoEmailForm()

    return render_to_response('registro.html',{"nuevoregistro":nuevoregistro,"add_nom_ape":add_nom_ape,"mensaje":mensaje,},context_instance=RequestContext(request))


def ingresar(request):
    mensaje=""
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/home')

    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    agregar_visita(usuario)
                    login(request, acceso)
                    response = HttpResponseRedirect('/home')
                    response.set_cookie("usuario",usuario)
                    response.set_cookie("use",acceso)
                    return response

                else:
                    mensaje=mensajes_no_activo
            else:
                mensaje=mensajes_error_login
        else:
            mensaje=mensajes_error_login
    else:
        formulario = AuthenticationForm()

    return render_to_response('ingresar.html',{'formulario':formulario,'mensaje':mensaje},context_instance=RequestContext(request))



def notas(request):
    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    notas=Notas.objects.filter(cedula=datos.cedula)
    materia=materias
    titulo_evaluacion=nombre_evaluacion
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()

    return render_to_response('notas.html',{'datos':datos,'numcomentarios':numcomentarios,'notas':notas,'materia':materia,'titulo':titulo_evaluacion},context_instance=RequestContext(request))

def NoNotas(request):
    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    mensaje=""
    if request.method == 'POST':
        imagenform=ImagenForm()
        reset=PasswordChangeForm(request.user)
        if request.POST['view'] == 'False':
            Notas.objects.filter(cedula=datos.cedula).update(ver=False)
        elif request.POST['view'] == 'True':
            Notas.objects.filter(cedula=datos.cedula).update(ver=True)
    else:
        reset=PasswordChangeForm(request.user)
        imagenform=ImagenForm()


    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()
    return render_to_response('perfil.html',{'datos':datos,'numcomentarios':numcomentarios,'mensaje':mensaje,'imagenform':imagenform,'reset':reset},context_instance=RequestContext(request))


def Todasnotas(request):
    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    notas=Notas.objects.all()
    materia=materias
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()

    return render_to_response('todasnotas.html',{'datos':datos,'numcomentarios':numcomentarios,'notas':notas,'materia':materia},context_instance=RequestContext(request))

def subirNotas(request):
    mensaje=""
    if request.method == 'POST':
        archivo=ArchivoForm(request.POST,request.FILES)
        if archivo.is_valid():
            nom=request.FILES['archivo']
            if permitir_extension(nom.name):
                nom.name='planilla.xls'
                p=Planillas.objects.create(archivo=nom)
                p.save
                nomarchivo=Planillas.objects.get(archivo='carga/%s'%(nom.name))
                ruta=nomarchivo.archivo.path
                planilla=AddNotas(ruta)

                if planilla.get_seccion() == 'A':
                    todas_cedulas=Cedulas.objects.all()
                    codigo_materia=planilla.get_codigo_materia()

                    #Agragamos la leyenda de las notas a la base de datos
                    lista_leyenda=[]
                    planilla.get_leyenda_notas(lista_leyenda)
                    agregar_leyenda(lista_leyenda,Leyenda,codigo_materia)

                    for cedula in todas_cedulas:
                        notas=[]
                        try:
                            planilla.get_notas(notas,cedula.cedula_user)
                            if notas:
                                try:
                                    ce=Cedulas.objects.get(cedula_user=cedula.cedula_user)
                                    nota=Notas.objects.get(cedula=ce)
                                    leyenda=Leyenda.objects.get(codigo=codigo_materia)

                                    if nota.cedula == ce and nota.codigo == codigo_materia:
                                        Notas.objects.filter(id=nota.id).update(leyenda=leyenda,nota1=notas[0],nota2=notas[1],nota3=notas[2],
                                                                 nota4=notas[3],nota5=notas[4],nota6=notas[5],
                                                                 nota7=notas[6],nota8=notas[7],nota9=notas[8],
                                                                 nota10=notas[9],nota11=notas[10],nota12=notas[11],
                                                                 notaDef=notas[12])
                                    else:
                                        com=Notas.objects.create(cedula=ce,leyenda=leyenda,codigo=codigo_materia,
                                                                 nota1=notas[0],nota2=notas[1],nota3=notas[2],
                                                                 nota4=notas[3],nota5=notas[4],nota6=notas[5],
                                                                 nota7=notas[6],nota8=notas[7],nota9=notas[8],
                                                                 nota10=notas[9],nota11=notas[10],nota12=notas[11],
                                                                 notaDef=notas[12])
                                        com.save()
                                except:
                                    ce=Cedulas.objects.get(cedula_user=cedula.cedula_user)
                                    leyenda=Leyenda.objects.get(codigo=codigo_materia)
                                    com=Notas.objects.create(cedula=ce,codigo=codigo_materia,leyenda=leyenda,
                                                             nota1=notas[0],nota2=notas[1],nota3=notas[2],
                                                             nota4=notas[3],nota5=notas[4],nota6=notas[5],
                                                             nota7=notas[6],nota8=notas[7],nota9=notas[8],
                                                             nota10=notas[9],nota11=notas[10],nota12=notas[11],
                                                             notaDef=notas[12])
                                    com.save()

                        except:
                            pass


                    #Borramos el archivo para no ocupar espacio
                    mensaje='exito'
                    os.remove(ruta)
                    Planillas.objects.filter(archivo='carga/%s'%(nom.name)).delete()

                else:
                    mensaje='seccion'
                    os.remove(ruta)
                    Planillas.objects.filter(archivo='carga/%s'%(nom.name)).delete()
            else:
                mensaje='extension'
    else:
        archivo=ArchivoForm()

    return render_to_response('subir.html',{'archivo':archivo,'mensaje':mensaje},context_instance=RequestContext(request))


def perfil(request):
    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()
    ##Formularios
    reset=PasswordChangeForm(request.user)
    imagenform=ImagenForm()

    return render_to_response('perfil.html',{'datos':datos,'numcomentarios':numcomentarios,'imagenform':imagenform,'reset':reset},context_instance=RequestContext(request))


def cambiarPass(request):
    mensaje=""
    if request.method == 'POST':
        imagenform=ImagenForm()
        reset=PasswordChangeForm(request.user,request.POST)
        if reset.is_valid():
            reset.save()
            mensaje="exito"
        else:
            mensaje="error"
    else:
        reset=PasswordChangeForm(request.user)
        imagenform=ImagenForm()

    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()

    return render_to_response('perfil.html',{'datos':datos,'numcomentarios':numcomentarios,'imagenform':imagenform,'reset':reset,'mensaje':mensaje},context_instance=RequestContext(request))

def cambiarImagen(request):
    mensaje=""
    if request.method == 'POST':
        reset=PasswordChangeForm(request.user)
        imagenform=ImagenForm(request.POST,request.FILES)
        if imagenform.is_valid():
            imagen=Usuarios.objects.get(usuario=request.user)
            imagen.imagen=request.FILES['imagen']
            imagen.save()
            mensaje="exito-img"
        else:
            mensaje="error-img"
    else:
        imagenform=ImagenForm()
        reset=PasswordChangeForm(request.user)


    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()

    return render_to_response('perfil.html',{'datos':datos,'numcomentarios':numcomentarios,'imagenform':imagenform,'reset':reset,'mensaje':mensaje},context_instance=RequestContext(request))

def eliminar(request):
    mensaje=""
    if request.method == 'POST':
        if request.POST['view'] == 'True':
            desactivar=User.objects.get(username=request.user)
            if desactivar.is_active != 0:
                desactivar.is_active=0
                desactivar.save()
                mensaje='exito'
            else:
                mensaje='error1'
        else:
            mensaje='error2'

    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()
    return render_to_response('eliminar.html',{'datos':datos,'numcomentarios':numcomentarios,'mensaje':mensaje},context_instance=RequestContext(request))

def comentario(request,id):
    comentario=get_object_or_404(Comentarios,pk=id)
    numcom=Comentarios.objects.all().filter(usuario=comentario.usuario).count()
    if comentario:
        return render_to_response('comentario.html',{'comentario':comentario,'numcom':numcom},context_instance=RequestContext(request))

    return HttpResponseRedirect('/home')



@login_required(login_url='/ingresar')
def home(request):
    user=request.user
    datos=Usuarios.objects.get(usuario=user.pk)
    numcomentarios=Comentarios.objects.all().filter(usuario=user.pk).count()
    if request.method == 'POST':
        com=ComentarioForm(request.POST)
        if com.is_valid():
            agregar_comentario(request,Comentarios,datos)
            return HttpResponseRedirect('/home')

    ComForm=ComentarioForm()
    comentarios=Comentarios.objects.all().order_by('-id')

    return render_to_response('comentarios.html',{'datos':datos,'numcomentarios':numcomentarios,'comform':ComForm,'comentarios':comentarios},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/ingresar')
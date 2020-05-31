from django.shortcuts import render, redirect
from django.http import HttpResponse
from pasantias.models import Empresa, Solicitud
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#pagina anonimo 

def index(request):
    #Obtiene las empresas
    lista_empresas = Empresa.objects.all()
    #Crea el contexto
    contexto = {
        'lista_empresas': lista_empresas
       
    }
    #Envia el contexto al template
    return render(request, 'pasantias/index.html', contexto)


#pagina coordinador

@login_required
def coordinador(request):
    #Obtiene las empresas y solicitudes
    lista_solicitudes = Solicitud.objects.all()
    lista_empresas = Empresa.objects.all()        
    #Crea el contexto
    contexto = {
        'lista_solicitudes': lista_solicitudes,
        'lista_empresas': lista_empresas
    }
    
    return render(request, 'pasantias/Coordinador.html', contexto)


#pagina estudiante

@login_required
def estudiante(request):
    #Obtiene las empresas
    lista_empresas = Empresa.objects.all()
    lista_solicitudes = Solicitud.objects.all()
    #Crea el contexto
    contexto = {
        'lista_solicitudes': lista_solicitudes,
        'lista_empresas': lista_empresas
        
    }
    #Envia el contexto al template
    return render(request, 'pasantias/Estudiante.html', contexto)


#Registro

def form_Reg(request):
    return render(request, 'pasantias/form_Reg.html')

def post_Reg(request):
    #obtiene la informacion del formulario
    username = request.POST['username']
    nombres = request.POST['first_name']
    apellidos = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    tipo = bool(request.POST['is_superuser'])

    #Crea el objeto
    usuario = User()
    usuario.username = username
    usuario.first_name = nombres
    usuario.last_name = apellidos
    usuario.email = email
    usuario.set_password(password)
    usuario.is_superuser = tipo 

    #guarda el objeto en la BD
    usuario.save()

    return redirect('pasantias:form_Ing')
    

#Login
    
def form_Ing(request):
    return render(request, 'pasantias/form_Ing.html')

def post_Ing(request):
    #obtiene la información del formulario
    u = request.POST['username']
    p = request.POST['password']
    tipo = bool(request.POST['is_superuser'])

    #Obtiene el usuario con los datos digitados
    usuario = authenticate(username=u, password=p)

    if usuario is not None:

        if tipo == True and usuario.is_superuser:

            login(request, usuario)
            return redirect('pasantias:coordinador')
                
        elif tipo == True and not usuario.is_superuser:

            return redirect('pasantias:form_Ing')
                
        elif tipo == False and usuario.is_superuser:

            return redirect('pasantias:form_Ing')
            
        elif tipo == False and not usuario.is_superuser:

            login(request, usuario)
            return redirect('pasantias:estudiante')
           
        else:
            return redirect('pasantias:form_Ing')
    else:
        return redirect('pasantias:form_Ing')
        #return render(request, 'pasantias/form_Ing')
        

#Logout

def view_logout(request):
    logout(request)
 
  # Redirecciona la página de login
    return redirect('pasantias:form_Ing')


#Crear convenio

def post_crea_convenio(request):
    n = request.POST['nombre']
    f = request.POST['facultad']

    empresa = Empresa(nombre=n, facultad=f)
    empresa.save()

    return redirect('pasantias:coordinador')


#Solicitar pasantia

def post_crea_solicitud(request):
    emp_id = request.POST['empresa_id']
    usu_id = request.user.id

    solicitud = Solicitud(empresa_id=emp_id, usuario_id=usu_id)
    solicitud.save()
    
    return redirect('pasantias:estudiante')


#Cambiar estado de solictud

def post_cambia_solicitud(request):
    estado = request.POST['cambio']
    id_solicitud = int(request.POST['id_c'])

    solicitud = Solicitud.objects.get(id=id_solicitud)
    solicitud.estado=estado
    solicitud.save()        
    
    return redirect('pasantias:coordinador')



from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm #,UserCreationForm
from django.contrib.auth import login as do_login
#from users.models import User #Nuestro modelo de usuarios personalizado
from users.admin import RegisterForm, RegisterStaffForm
from users.models import User

#from django.contrib.auth import get_user_model


# Create your views here.
def home_page(request):
    # si estamos identificados devolvemos al home
    if request.user.is_authenticated:
        return render(request, 'home_page.html')
    # En caso contrario redireccionamos a login
    return redirect('/login')

def login(request):
    form = User()
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = RegisterForm()
    user = None
    if request.method == "POST":

        # Añadimos los datos recibidos al formulario
        form = RegisterForm(data = request.POST)

        # Si el formulario es válido...
        if form.is_valid():
        # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente
        if user is not None:
            # Hacemos el login manualmente
            do_login(request, user)
            # Y le redireccionamos a la portada
            return redirect('/')
    # Si queremos borramos los campos de ayuda
    #form.fields['Username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})


def registerStaff(request):
    # Creamos el formulario de autenticación vacío
    form = RegisterStaffForm()
    user = None
    if request.method == "POST":

        # Añadimos los datos recibidos al formulario
        form = RegisterStaffForm(data = request.POST)

        # Si el formulario es válido...
        if form.is_valid():
        # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente
        if user is not None:
            # Hacemos el login manualmente
            do_login(request, user)
            # Y le redireccionamos a la portada
            return redirect('/')
    # Si queremos borramos los campos de ayuda
    #form.fields['Username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "registerStaff.html", {'form': form})
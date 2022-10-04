from django.shortcuts import render
# trae formulario de registro o signup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
# login= crea cookie para mantener inicio de sesion, con esta funsion se puede crear una cookie para manter la secion aciva
from django.contrib.auth import login, logout, authenticate # logut= sirve para cerrar la secion
# authenticate= sirve para verificar que el usuario exista y la contraseña este correcta e iniciar secion
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError

#registrarce
def signup(request):
    if request.method == 'GET':
        return render(request, "singup.html", {'form': UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()

                login(request, user)

                return redirect("tasks")
            except IntegrityError:
                return render(request, "singup.html", {'form': UserCreationForm, "error": "User already exist "})
        else:
            return render(request, "singup.html", {'form': UserCreationForm, "error": "Password do not match"})

# cerrar session
@login_required
def logout_session(request):
    logout(request)
    return redirect("home")
# inicio sesion
def login_session(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "login.html", {"form": AuthenticationForm,
                                                  "error": "Username o password is incorrect"})
        else:
            login(request, user)
            return redirect("tasks")

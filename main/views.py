from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, "index.html")


def main_view(request):
    return render(request, "main.html")


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(
            f"Intentando iniciar sesión con usuario: {username}"
        )  # Log del nombre de usuario

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Inicio de sesión exitoso")  # Log de inicio de sesión exitoso
            return redirect("main")
        else:
            print("Falló el inicio de sesión")  # Log de fallo de inicio de sesión
            return render(
                request,
                "registration/login.html",
                {"error": "Credenciales incorrectas"},
            )
    else:
        return render(request, "registration/login.html")

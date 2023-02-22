import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from proveedores_app.functions import *
from proveedores_app.forms import proveedoresForm
from proveedores_app.models import Proveedores

@login_required(login_url="/sign-in")
def formulario_archivos(request):
    if request.method == 'POST':
        proveedor = proveedoresForm(request.POST, request.FILES)
        proveedores = Proveedores()
        usuario = User.objects.get(username=request.user)
        if proveedor.is_valid():
            proveedores.bfirstname = usuario.first_name
            proveedores.bemail = usuario.email
            proveedores.bnit = usuario.last_name
            proveedores.id_usr = usuario
            handle_uploaded_file(request.FILES['file'], proveedores.bnit)
            handle_uploaded_file2(request.FILES['file2'], proveedores.bnit)
            handle_uploaded_file3(request.FILES['file3'], proveedores.bnit)
            handle_uploaded_file4(request.FILES['file4'], proveedores.bnit)
            proveedores.bfile = True
            proveedores.bfile2 = True
            proveedores.bfile3 = True
            proveedores.bfile4 = True
            proveedores.fecha_s = datetime.date.today()
            proveedores.save()

            text = "Archivos cargados correctamente"
            icon = "success"
            request.session['text'] = {'text': text, 'icon': icon}
            return HttpResponseRedirect(reverse("inicio"))
    else:
        proveedores = proveedoresForm()
        return render(request, "form/form_files.html", {'form': proveedores})


@login_required(login_url="/signin")
def index(request):
    if request.method == 'GET':
        usuario = User.objects.get(username=request.user)
        if 'text' in request.session:
            text_s = request.session['text']
            text = text_s['text']
            icon = text_s['icon']

            del request.session['text']
        else:
            text = ""
            icon = ""

    return render(request, 'dashboard/index.html', {'text': text, 'icon': icon, 'user': usuario})


def signup(request):
    if request.method == 'GET':
        if 'text' in request.session:
            text_s = request.session['text']
            text = text_s['text']
            icon = text_s['icon']
            del request.session['text']
        else:
            text = "Registre sus datos"
            icon = "info"

        return render(request, 'dashboard/auth/sign-up.html', {'text': text, 'icon': icon})

    if request.method == "POST":
        username = request.POST['username']
        rsocial = request.POST['rsocial']
        nit = request.POST['nit']
        email = request.POST['email']
        passw1 = request.POST['passw1']
        passw2 = request.POST['passw2']
        if passw1 == passw2:
            myuser = User.objects.create_user(username, email, passw1)
            myuser.first_name = rsocial
            myuser.last_name = nit

            myuser.save()
            text = "Se creo correctamente su cuenta"
            icon = "success"
        else:
            text = "Las contraseñas no coinciden"
            icon = "error"

        return render(request, 'dashboard/auth/sign-up.html', {'text': text, 'icon': icon})
    else:
        return render(request, 'dashboard/auth/sign-up.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        passw1 = request.POST['passw1']

        user = authenticate(username=username, password=passw1)

        if user is not None:
            login(request, user)
            rsocial = user.first_name
            aviso = "Inicio de sesión, exitoso!"
            ind = 2
            return HttpResponseRedirect(reverse('inicio'), {'rsocial': rsocial, 'aviso': aviso, 'ind': ind})
        else:
            aviso = "Credenciales incorrectas"
            ind = 0
            request.session['aviso'] = {'aviso': aviso, 'ind': ind}
            return redirect('/dashboard/auth/sign-in.html')

    return render(request, "dashboard/auth/sign-in.html")


def signout(request):
    logout(request)
    text = "Cierre de sesión exitoso"
    icon = 'success'
    request.session['text'] = {'text': text, 'icon': icon}
    return redirect('sign-in')

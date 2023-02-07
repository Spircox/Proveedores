from django import forms


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Ingrese primer nombre", max_length=20)
    lastname = forms.CharField(label="Ingrese apellido", max_length=20)
    email = forms.EmailField(label="Ingrese correo electronico")
    nit = forms.CharField(label="Ingrese numero de NIT", max_length=15)
    file = forms.FileField(label="Camara de Comercio")  # for creating file input
    file2 = forms.FileField(label="RUT")

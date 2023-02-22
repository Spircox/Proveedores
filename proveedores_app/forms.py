from django import forms


class proveedoresForm(forms.Form):
    file = forms.FileField(label="1")  # for creating file input
    file2 = forms.FileField(label="2")
    file3 = forms.FileField(label="3")
    file4 = forms.FileField(label="4")

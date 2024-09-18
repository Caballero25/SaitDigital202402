from django import forms
from django.core.validators import FileExtensionValidator


class DocumentForm(forms.Form):
    pdf = forms.FileField(label="Seleccionar PDF", 
                          validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                          widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}))
    p12 = forms.FileField(label="Seleccionar Firma Electrónica (.p12)", 
                          validators=[FileExtensionValidator(allowed_extensions=['p12'])],
                          widget=forms.ClearableFileInput(attrs={'accept': '.p12'}))
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

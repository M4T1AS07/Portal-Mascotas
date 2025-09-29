from django import forms
from .models import SolicitudAdopcion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ["nombre_completo", "email", "telefono", "direccion", "motivo"]
        widgets = {
            "nombre_completo": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "motivo": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

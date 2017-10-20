from django import forms;
class MonedasForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de la moneda'
        }),
        label="NOMBRE",
        max_length=30
        )
    abreviacion = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Abreviacion'
        }),
        label="Abreviación",
        max_length=3
        )

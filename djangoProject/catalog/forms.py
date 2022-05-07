from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateTimeInput, DateInput, Select

from catalog.models import Catalog

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ['nume_elev', 'nota_elev','materie']
        widgets = {
            'nume_elev':TextInput(attrs={'class':'form-control','placeholder':'student names','id':'tags'}),
            'nota_elev':TextInput(attrs={'class':'form-control','placeholder':'Enter student\'s grade'}),
            'materie':Select(attrs={'class':'form-control','placeholder':'select course'})
        }


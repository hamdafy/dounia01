from django import forms
from.models import Patient00

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient00
        fields=['name','vorname','alter','motif']
        labels={'name':'nom',
                'vorname':'prenom',
                'alter':'age',
                'Motif':'le motif de la visite',



        }


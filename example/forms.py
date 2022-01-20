from django import forms
from django.core.exceptions import ValidationError

from .helpers import parse_csv


class FirstForm(forms.Form):
    file = forms.FileField(label="Fichier CSV", required=True)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        """Nettoie les données du fichier reçu."""
        super().clean()
        uploaded = parse_csv(self.request.FILES['file'])
        if not uploaded['names'] or not uploaded['data']:
            raise ValidationError("Uploaded data is invalid")
        self.request.session['uploaded'] = uploaded


class SecondForm(forms.Form):
    columns = forms.MultipleChoiceField(label="Colonnes")

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.uploaded = request.session['uploaded']
        self.fields['columns'].choices = [
            (id_, name)
            for id_, name in enumerate(self.uploaded['names'], start=1)
        ]

    def clean_columns(self):
        """Valide les données sur les columns et transforme les choix en int."""
        columns = self.cleaned_data['columns']
        return [int(column) for column in columns]

    def clean(self):
        super().clean()
        self.request.session['selection'] = self.cleaned_data['columns']

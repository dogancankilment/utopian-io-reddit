from django import forms
from choices import *


class ChoiceForm(forms.Form):
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)

    def clean_form(self):
        return self.cleaned_data
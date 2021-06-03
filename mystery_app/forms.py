from django import forms
from mystery_app.models import Guess


class GuessForm(forms.ModelForm):
    class Meta:
        model = Guess
        fields = ['word']

from django import forms
from django.core.validators import RegexValidator

# form where player enters guess
class InputForm(forms.Form):
    # player can only enter one letter at a time;
    # ignore repeated letters and non-alphabetic symbols
    letter = forms.CharField(
        required=False,
        max_length=1,
        label='',
        help_text='\n',
        validators=[RegexValidator('[a-zA-Z]')],
        widget=forms.TextInput(attrs={
            'autofocus': 'autofocus',
            'autocomplete':'off',
            'size': 15,
            'placeholder': 'Enter letter'
        }))
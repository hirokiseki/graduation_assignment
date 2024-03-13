from django import forms

class InputForm(forms.Form):
    math_formula = forms.CharField(label='式')
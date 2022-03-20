from django import forms

class OptionsForm(forms.Form):
    dir = forms.CharField(label='Your name', max_length=100 ,default="up" ) 
    sector = forms.CharField(label='Your name', max_length=100)
    sortBy = forms.CharField(label='Your name', max_length=100)
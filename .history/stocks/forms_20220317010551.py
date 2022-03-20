from django import forms

class OptionsForm(forms.Form):
    sortDirection = forms.ChoiceField() 
    sector = forms.CharField(label='sector', max_length=100)
    sortBy = forms.CharField(label='sortby', max_length=100)
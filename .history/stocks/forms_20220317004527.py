from django import forms

class OptionsForm(forms.Form):
    xxx = forms.CharField(label='sort direction', max_length=100 ) 
    sector = forms.CharField(label='sector', max_length=100)
    sortBy = forms.CharField(label='sortby', max_length=100)
from django import forms
GEEKS_CHOICES =(
    ("1", "Up"),
    ("2", "Down"),

)

class OptionsForm(forms.Form):
    sortDirection = forms.ChoiceField(choices=['up','down']) 
    sector = forms.CharField(label='sector', max_length=100)
    sortBy = forms.CharField(label='sortby', max_length=100)
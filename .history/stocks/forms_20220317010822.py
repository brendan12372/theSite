from django import forms
CHOICES =(
    ("1", "Up"),
    ("2", "Down"),

)

class OptionsForm(forms.Form):
    sortDirection = forms.ChoiceField(choices=CHOICES) 
    sector = forms.CharField(label='sector', max_length=100)
    sortBy = forms.CharField(label='sortby', max_length=100)
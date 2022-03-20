from django import forms
SORT_CHOICES =(
    ("1", "Up"),
    ("2", "Down"),
)

SECTOR_CHOICES =(
    ("1", "Technoloy"),
    ("2", "Down"),
)


class OptionsForm(forms.Form):
    sortDirection = forms.ChoiceField(choices=CHOICES) 
    sector = forms.CharField(label='sector', max_length=100)
    sortBy = forms.CharField(label='sortby', max_length=100)
from django import forms
sectorList = (
    ('Basic%20Materials':"Basic%20Materials"),
    ('Consumer%20Defensive':"Consumer Defensive") ,
    ('Healthcare':'Healthcare'), ('Communication%20Services':'Communication Services'), ('Energy':"Energy"),
    ('Industrials':'Industrials'),
    ('Consumer%20Cyclical',"Consumer Cyclical"), ('Financial%20Services':'FinancialServices'), ('Technology':'Technology'))

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
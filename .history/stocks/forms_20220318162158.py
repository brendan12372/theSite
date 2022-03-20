from django import forms
sectorList = (
    ('all','all')
    ('Basic%20Materials',"Basic Materials"),
    ('Consumer%20Defensive',"Consumer Defensive") ,
    ('Healthcare','Healthcare'), ('Communication%20Services','Communication Services'), ('Energy',"Energy"),
    ('Industrials','Industrials'),
    ('Consumer%20Cyclical',"Consumer Cyclical"), ('Financial%20Services','FinancialServices'), ('Technology','Technology'))

SORT_CHOICES =(
    ("up", "up"),
    ("down", "down"),
)

SORT_CHOICES2 =(
    ("yearReturn", "yearReturn"),
    ("marketCap", "marketCap"),
    ("pegRatio", "pegRatio"),
)


class OptionsForm(forms.Form):
    sortDirection = forms.ChoiceField(choices=SORT_CHOICES) 
    sector = forms.ChoiceField(choices=sectorList)
    sortBy = forms.ChoiceField(choices=SORT_CHOICES2)
    
    class Meta:
        fields = ['sector','sortBy','sortDirection']
from django import forms




sectorList = (
    ('Basic%20Materials',"Basic Materials"),
    ('Consumer%20Defensive',"Consumer Defensive") ,
    ('Healthcare','Healthcare'), ('Communication%20Services','Communication Services'), ('Energy',"Energy"),
    ('Industrials','Industrials'),
    ('Consumer%20Cyclical',"Consumer Cyclical"), ('Financial%20Services','FinancialServices'), ('Technology','Technology'))

SORT_CHOICES =(
    ("1", "Up"),
    ("2", "Down"),
)

SORT_CHOICES2 =(
    ("1", "YearReturn"),
    ("2", "MarketCap"),
    ("3", "pegRatio"),
)


class OptionsForm(forms.Form):
    sortDirection = forms.ChoiceField(choices=SORT_CHOICES) 
    sector = forms.ChoiceField(choices=sectorList)
    sortBy = forms.ChoiceField(choices=SORT_CHOICES2)
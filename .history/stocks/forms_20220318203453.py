from django import forms
from .models import Stock
from .serializers import StockSerializer
x=Stock.objects.get(symbol='aapl')
print(x.get_model_fields().to_dict)
sectorList = (
    ('all','all'),
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
    x=Stock.objects.get_or_create(symbol='aapl')
    
    sortDirection = forms.ChoiceField(choices=SORT_CHOICES) 
    sector = forms.ChoiceField(choices=sectorList)
    sortBy = forms.ChoiceField(choices=SORT_CHOICES2)
    
    class Meta:
        fields = ['sector','sortBy','sortDirection']
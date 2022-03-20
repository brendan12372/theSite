from django import forms
from .models import Stock
from .serializers import StockSerializer
x=Stock.objects.get(symbol='aapl')
print(x.get_model_fields())

sectorList = (
    ('all','all'),
    ('Basic Materials',"Basic Materials"),
    ('Consumer Defensive',"Consumer Defensive") ,
    ('Healthcare','Healthcare'), ('Communication Services','Communication Services'), ('Energy',"Energy"),
    ('Industrials','Industrials'),
    ('Consumer Cyclical',"Consumer Cyclical"), ('Financial Services','FinancialServices'), ('Technology','Technology'))

SORT_CHOICES =(
 
    ("down", "down"),   ("up", "up"),
)


ml= [ 'fullTimeEmployees',  'ebitdaMargins', 'profitMargins',
         'grossMargins', 'operatingCashflow', 'revenueGrowth', 'operatingMargins', 'ebitda', 'targetLowPrice',
         'recommendationKey', 'grossProfits', 'freeCashflow', 'targetMedianPrice', 'currentPrice', 'earningsGrowth',
         'currentRatio', 'returnOnAssets', 'numberOfAnalystOpinions', 'targetMeanPrice', 'debtToEquity',
         'returnOnEquity', 'targetHighPrice', 'totalCash', 'totalDebt', 'totalRevenue', 'totalCashPerShare',
         'financialCurrency', 'revenuePerShare', 'quickRatio', 'recommendationMean', 'exchange', 'shortName',
         'longName', 'exchangeTimezoneName', 'exchangeTimezoneShortName', 'isEsgPopulated', 'gmtOffSetMilliseconds',
         'quoteType', 'symbol', 'messageBoardId', 'market', 'annualHoldingsTurnover', 'enterpriseToRevenue',
         'beta3Year', 'enterpriseToEbitda', '52WeekChange', 'morningStarRiskRating', 'forwardEps',
         'revenueQuarterlyGrowth', 'sharesOutstanding', 'fundInceptionDate', 'annualReportExpenseRatio', 'totalAssets',
         'bookValue', 'sharesShort', 'sharesPercentSharesOut', 'fundFamily', 'lastFiscalYearEnd',
         'heldPercentInstitutions', 'netIncomeToCommon', 'trailingEps', 'lastDividendValue', 'SandP52WeekChange',
         'PriceToBook', 'heldPercentInsiders', 'nextFiscalYearEnd', 'yield', 'mostRecentQuarter', 'shortRatio',
         'sharesShortPreviousMonthDate', 'floatShares', 'beta', 'enterpriseValue', 'priceHint',
         'threeYearAverageReturn', 'lastSplitDate', 'lastSplitFactor', 'legalType', 'lastDividendDate',
         'morningStarOverallRating', 'earningsQuarterlyGrowth', 'priceToSalesTrailing12Months', 'dateShortInterest',
         'pegRatio', 'ytdReturn', 'forwardPE', 'lastCapGain', 'shortPercentOfFloat', 'sharesShortPriorMonth',
         'impliedSharesOutstanding', 'category', 'fiveYearAverageReturn', 'previousClose', 'regularMarketOpen',
         'twoHundredDayAverage', 'trailingAnnualDividendYield', 'payoutRatio', 'volume24Hr', 'regularMarketDayHigh',
         'navPrice', 'averageDailyVolume10Day', 'regularMarketPreviousClose', 'fiftyDayAverage',
         'trailingAnnualDividendRate', 'open', 'toCurrency', 'averageVolume10days', 'expireDate', 'algorithm',
         'dividendRate', 'exDividendDate', 'circulatingSupply', 'startDate', 'regularMarketDayLow', 'currency',
         'regularMarketVolume', 'lastMarket', 'maxSupply', 'openInterest', 'marketCap', 'volumeAllCurrencies',
         'strikePrice', 'averageVolume', 'dayLow', 'ask', 'askSize', 'volume', 'fiftyTwoWeekHigh', 'fromCurrency',
     ]
SORT_CHOICES2=[]
for m in ml:
    SORT_CHOICES2.append((m,m))

# SORT_CHOICES2 =(
#     ("yearReturn", "yearReturn"),
#     ("marketCap", "marketCap"),
#     ("pegRatio", "pegRatio"),
#     ()
# )

# s = Stock('appl')
# f = []
# f = s.get_model_fields()
# fl=[]
# for m in f:
#     fl.append(m.name)

# for m in f:
#     SORT_CHOICES2.append((m.name,m.name))


class OptionsForm(forms.Form):
    
    
    sortDirection = forms.ChoiceField(choices=SORT_CHOICES) 
    sector = forms.ChoiceField(choices=sectorList)
    sortBy = forms.ChoiceField(choices=SORT_CHOICES2)
    
    class Meta:
        fields = ['sector','sortBy','sortDirection']
        
class sForm(forms.Form):
    symbol = forms.CharField() 

    
    class Meta:
        fields = ['symbol']
        

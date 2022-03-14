from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from statistics import mean
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

from django.db import models
from pyFundamental.utils import Stock as St
# # Create your models here.
class Mysector(models.Model):
    name=models.CharField(max_length=200, unique=True)
    ave = models.FloatField(default=0, blank=True, null=True)
    def get_ave(self,sortBy):
        stocks = Stock.objects.filter(sector=self.name)
        vals=stocks.values_list(sortBy)
        ave_list=[]
        for val in vals:
            ave_list.append(val[0])
        self.ave=mean(ave_list)
        self.save()
        print(f'{self.name} {self.ave}')



    def __str__(self):
        return self.name


class Stock(models.Model):
    symbol = models.CharField(max_length=200, unique=True)
    ebitdaMargins = models.FloatField(default=0, blank=True, null=True)
    sector = models.CharField(max_length=200, blank=True)
    floatShares=models.IntegerField(default=0, blank=True, null=True)
    
    targetPriceLow=models.IntegerField(default=0, blank=True, null=True)

    
    grossMargins = models.FloatField(default=0,blank=True, null=True)
    profitMargins = models.FloatField(default=0,blank=True, null=True)
    grossProfits=models.IntegerField(default=0, blank=True, null=True)
    bookValue=models.FloatField(default=0, blank=True, null=True)
    forwardEPS=models.FloatField(default=0, blank=True, null=True)
    trailingEPS=models.FloatField(default=0, blank=True, null=True)




    yearReturn = models.FloatField(blank=True, null=True)
    pegRatio = models.FloatField(default=0, blank=True, null=True)
    ave = models.FloatField(default=0, blank=True, null=True)
    shortPercentOfFloat = models.FloatField(default=0, blank=True, null=True)
    marketCap = models.IntegerField(default=0, blank=True, null=True)
    payoutRatio = models.FloatField(blank=True, null=True)
    fullTimeEmployees = models.IntegerField(blank=True, null=True)
    trailingEPS = models.FloatField(default=0, blank=True, null=True)
    forwardEPS = models.FloatField(default=0, blank=True, null=True)
    forwardPE = models.FloatField(default=0, blank=True, null=True)
    PriceToBook = models.FloatField(default=0, blank=True, null=True)
    returnOnEquity= models.FloatField(default=0, blank=True, null=True)
    currentRatio = models.FloatField(default=0, blank=True, null=True)
    debtEquityRatio = models.FloatField(default=0, blank=True, null=True)
    insiders = models.FloatField(default=0,null=True,blank=True)
    tcps = models.FloatField(default=0,null=True,blank=True)
    quickRatio = models.FloatField(default=0, blank=True, null=True)
    shortName = models.CharField(max_length=222, default='', blank=True)
    beta = models.FloatField(blank=True, null=True)
    sharesPercentSharesOut = models.FloatField(default=0,null=True,blank=True)
    averageVolume=models.IntegerField(default=0,null=True,blank=True)
    averageVolume10days = models.IntegerField(default=0,null=True,blank=True)
    bidSize = models.IntegerField(default=0,null=True)
    currentPrice = models.FloatField(default=0,null=True,blank=True)
    dividendRate=models.FloatField(default=0,null=True,blank=True)
    dividendYield=models.FloatField(default=0,null=True,blank=True)
    earningsQuarterlyGrowth=models.FloatField(default=0,null=True,blank=True)
    ebitda=models.IntegerField(default=0,null=True,blank=True)
    enterpriseToEbitda=models.FloatField(default=0,null=True,blank=True)
    enterpriseToRevenue=models.FloatField(default=0,null=True,blank=True)
    enterpriseValue=models.FloatField(default=0,null=True,blank=True)
    fiftyDayAverage=models.FloatField(default=0,null=True,blank=True)
    fiftyTwoWeekHigh=models.FloatField(default=0,null=True,blank=True)
    fiftyTwoWeekLow=models.FloatField(default=0,null=True,blank=True)
    fiveYearAvgDividendYield=models.FloatField(default=0,null=True,blank=True)
    freeCashflow=models.IntegerField(default=0,null=True,blank=True)
    operatingCashflow=models.IntegerField(default=0,null=True,blank=True)
    operatingMargins=models.FloatField(default=0,null=True,blank=True)
    recommendationMean=models.FloatField(default=0,null=True,blank=True)
    revenueGrowth=models.FloatField(default=0,blank=True)
    revenuePerShare=models.FloatField(default=0,null=True,blank=True)
    totalCashPerShare=models.FloatField(default=0,null=True,blank=True)
    totalRevenue=models.IntegerField(default=0,null=True,blank=True)
    trailingAnnualDividendRate=models.FloatField(blank=True,default=0,null=True)
    trailingPE=models.FloatField(default=0,null=True,blank=True)
    forwardPE=models.FloatField(blank=True,null=True)
    twoHundredDayAverage=models.FloatField(blank=True,default=0,null=True)
    news=models.TextField(blank=True,null=True)
    link=models.models.CharField(blank=True,null=True, max_length=200)
    summary=models.TextField(blank=True,null=True)
    priceToSalesTrailing12Months=models.FloatField(blank=True,null=True,default=0)
    totalDebt=models.IntegerField(blank=True,null=True,default=0)
    totalCash=models.IntegerField(blank=True,null=True,default=0)
    myzero=models.IntegerField(blank=0,null=True,default=0)





    def getValue(self):
        S = St(self.symbol)
        self.sector = S.sector
        self.totalCash=S.info['totalCash']
        self.link=S.link
        self.priceToSalesTrailing12Months=round(S.info['priceToSalesTrailing12Months'],2)
        self.totalDebt=S.info['totalDebt']
        self.ebitdaMargins=round(S.info['ebitdaMargins'],2)
        self.fullTimeEmployees=S.fullTimeEmployees
        self.floatShares=S.info['floatShares']
        self.sharesShortPriorMonth=S.info['sharesShortPriorMonth']
        self.dividendRate=S.info['dividendRate']
        self.dividendYield = S.info['dividendYield']
        self.averageVolume = S.info['averageVolume']
        self.averageVolume10days = S.info['averageVolume10days']
        self.bidSize = S.bidSize
        self.currentPrice = S.info['currentPrice']
        self.dividendYield = S.info['dividendYield']
        self.earningsQuarterlyGrowth = S.info['earningsQuarterlyGrowth']
        self.ebitda = S.ebitda
        self.enterpriseToEbitda = round(S.info['enterpriseToEbitda'],2)
        self.enterpriseToRevenue = round(S.info['enterpriseToRevenue'],2)
        self.enterpriseValue = round(S.info['enterpriseValue'],2)
        self.trailingEPS = round(S.teps,2)
        self.payoutRatio = round(S.info['payoutRatio'],2)
        try:
            self.forwardEPS = S.feps
        except:
            self.forwardEPS=0
        try:
            self.forwardPE = S.fpe
        except:
            self.forwardPE=0
        self.yearReturn=S.yearReturn
        self.pegRatio=round(S.pegRatio,2)
        self.marketCap=S.marketCap
        self.fullTimeEmployees=S.fullTimeEmployees
        self.shortPercentOfFloat=S.shortPercentOfFloat
        try:
            self.fiftyDayAverage=S.fiftyDayAverage
        except:
            self.fiftyDayAverage=0
        self.twoHundredDayAverage=round(S.info['twoHundredDayAverage'],2)
        try:
            self.freeCashflow=S.freeCashflow
        except:
            self.freeCashflow=0
        self.operatingMargins=S.operatingMargins
        try:
            self.totalRevenue=S.info['totalRevenue']
        except:
            self.totalRevenue=0
        try:
            self.recommendationMean=S.recommendationMean
        except :
            self.recommendationMean=0
        self.news=S.news
        try:
            self.EbitdaMargins=round(S.info["ebitdaMargins"],2)
        except:
            self.EbitdaMargins=0
        try:
            self.trailingPE = round(S.info['trailingPE'],2)
        except:
            self.trailingPE=0 
        try:
            self.forwardPE = round(S.info["forwardPE"],2)
        except :
            self.forwardPE=0
        try:
            self.beta=round(S.info["beta"],2)
        except:
            self.beta=self.myzero
        self.summary=S.longBusinesSummary
        try:
            self.earningsQuarterlyGrowth=round(S.info['earningsQuarterlyGrowth'],2)
        except:
            self.earningsQuarterlyGrowth=0
            
        self.operatingCashflow=S.operatingCashflow
        try:
            self.totalCashPerShare=S.info["totalCashPerShare"]
        except :
            self.totalCashPerShare=0
        try:
            
            self.fiftyTwoWeekLow=round(S.info["fiftyTwoWeekLow"],2)
        except:
            self.fiftyTwoWeekLow=0
        try:
            self.fiftyTwoWeekHigh=S.fiftyTwoWeekHigh
        except :
            self.fiftyTwoWeekHigh=0
        try:
            self.trailingAnnualDividendRate=S.trailingAnnualDividendRate
        except :
            self.fiftyTwoWeekHigh=self.myzero
        try:
            self.dividendRate=round(S.info["dividendRate"],3)
        except :
            self.dividendRate=0
        try:
            self.dividendYield=round(S.info["dividendYield"]*100,3)
        except:
            self.dividendYield=0
        try:
            self.revenueGrowth=S.revenueGrowth
        except:
            self.revenueGrowth=0
        try:
            self.revenuePerShare = round(S.revenuePerShare,2)
        except:
            self.revenuePerShare=0
        try:
            self.fiveYearAvgDividendYield = S.fiveYearAvgDividendYield
        except :
            self.fiveYearAvgDividendYield=0
        try:
            self.sharesPercentSharesOut=S.sharesPercentSharesOut
        except :
            self.sharesPercentSharesOut=0

        try:
            self.PriceToBook = round(S.ptb,2)
        except:
            pass
        try:
            self.returnOnEquity = round(S.roe,2)
        except:
            pass
        try:
            self.currentRatio = round(S.currentRatio,2)
        except:
            self.currentRatio = 0
        try:
            self.debtEquityRatio = round(S.debtEquityRatio,2)
        except:
            pass
        try:
            self.insiders = round(S.insiders,2)
        except:
            pass
        try:
            self.tcps = round(S.tcps,2)
        except:
            pass
        try:
            self.quickRatio = round(S.quickRatio,2)
        except:
            self.quickRatio = 0
        try:
            self.shortName = S.shortName
        except:
            self.shortName = S.symbol
        try:
            self.beta = round(S.beta,2)
        except:
            self.beta=None
            
            
        
        try:
            self.profitMargins = round(S.profitMargins,2)
        except:
            self.profitMargins=None
            
        try:
            self.grossProfits = round(S.info["grossProfits"],2)
        except:
            self.grossProfits=None
            
            
                
        try:
            self.grossMargins = round(S.grossMargins,2)
        except:
            self.grossMargins=None
            
            
        try:
            self.bookValue = S.info['bookValue']
        except:
            self.bookValue=None





            
        try:
            self.forwardEPS = S.feps
        except:
            self.forwardEPS=None
            
            
        try:
            self.trailingEPS = S.teps
        except:
            self.trailingEPS=None
            
            




    # grossMargins = models.FloatField(,defualt=0,blank=True, null=True)
    # profitMargins = models.FloatField(defualt=0,blank=True, null=True)
    # grossProfits=models.IntegerField(default=0, blank=True, null=True)










    def __str__(self):
        return self.symbol

    def save(self, *args, **kwargs):
        print('save')
        self.getValue()
        super(Stock, self).save(*args, **kwargs)

    def get_model_fields(self):
        return self._meta.fields




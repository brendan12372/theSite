import pickle,re
from io import BytesIO
from statistics import mean
import requests
import yfinance as yf
from PIL import Image

curentList = []

import json, os
import pandas as pd
from random import randrange

def news():
    r = requests.get(f'http://72.14.185.11/all/marketCap/down').json()
    i=randrange(10)
    s=r[i]["symbol"]
    l=r[i]
    # print(r[i].keys())
    r=r[i]["news"]
    print(r)
    x=re.split("title",r)
    l=re.split("'link': '",r)
    y=re.split("publisher",x[1])
    z=re.split("'",y[0])
    return [z[2],s,l]
key_l = ['zip', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'city', 'phone', 'state', 'country',
         'companyOfficers', 'website', 'maxAge', 'address1', 'industry', 'address2', 'ebitdaMargins', 'profitMargins',
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
         'priceToBook', 'heldPercentInsiders', 'nextFiscalYearEnd', 'yield', 'mostRecentQuarter', 'shortRatio',
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
         'fiveYearAvgDividendYield', 'fiftyTwoWeekLow', 'bid', 'tradeable', 'dividendYield', 'bidSize', 'dayHigh',
         'regularMarketPrice', 'preMarketPrice', 'logo_url']


def makeDir():
    curDir = os.getcwd()
    try:
        os.mkdir('sectorData')
        os.mkdir('data')

    except Exception as e:
        print(e)

    dataDir = os.path.join(curDir, 'data')
    sectorDataDir = os.path.join(curDir, 'SectorData')


def temp(sortBy='yearReturn'):
    dfList = []
    x = []
    y = []
    z = []
    sectorList = []
    sl = []
    for a, b, c in os.walk(dataDir):
        z.append(a)
        sectorList.append(b)
        sl.append(c)
        fileList = []
    fileList = sl

    # print(fileList)
    sectorList = sectorList[0]
    # print(sectorList)
    sector = sectorList[4]  ####change
    fileList = []
    filePathList = []
    for i in range(len(sl) - 1):
        sectorPath = os.path.join(sectorDataDir, sector)
        fileList.append(sl[i + 1])
    myDict = dict(zip(sectorList, fileList))
    x = myDict
    keys = list(x.keys())
    vals = list(x.values())
    # print(keys)
    # print(vals)
    symbol_list = []
    for i in range(len(keys)):
        x = vals

    # print(keys)
    # print(x)
    for i in range(len(keys)):

        key = keys[i]
        # print(key)
        symbols = []
        vl = []
        na = sortBy

        for val in x[i]:
            message = val

            # check if the message ends with fun
            if message.endswith('json'):
                p = os.path.join(dataDir, key, val)

                # JSON file
                # print(p)

                f = open(p)

                # Reading from file
                data = json.loads(f.read())

                # print(f"{data['symbol']} {data['yearReturn']}")
                symbols.append(data['symbol'])
                symbol_list.append(data['symbol'])
                vl.append(data[na])

        data = {
            "symbols": symbols,
            na: vl
        }
        df = pd.DataFrame(data)
        # df['rank']=df.yearReturn.sort()
        dfList.append(df)

        df = df.sort_values(by=na, ascending=False)
        print(df)
        try:
            p = os.path.join(sectorDataDir, sortBy)
            os.mkdir(p)

        except Exception as e:
            # print(f'89 {e}')
            pass
        p = os.path.join(p, f'{key}.csv')
        df.to_csv(p)

    import pickle
    with open('universe.pickel', 'wb') as f:
        pickle.dump(symbol_list, f)
    # with open("universe.txt", 'w') as f:
    #     for item in symbol_list:
    #         f.write("%s\n" % item)


curDir = os.getcwd()
try:
    os.mkdir('data')
except:
    pass
dataDir = os.path.join(curDir, 'data')
sectorDataDir = os.path.join(curDir, 'sectorData')


class Stock:
    def __init__(self, symbol, p='1y'):
        self.path = dataDir
        curentList.append(symbol)
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
        self.info = self.ticker.info
        self.sector = self.info['sector']
        try:
            self.sectorDir = os.path.join(dataDir, self.sector)
            os.mkdir(self.sectorDir)
        except:
            pass
        self.filePath = os.path.join(dataDir, self.sector, self.symbol) + '.json'
        self.hist = self.ticker.history(period=p)
        try:
            self.news = self.ticker.news[0]["title"]
            self.link=self.ticker.news[0]["link"]
            
        except:
            print(f'err:  {ticker.news}')
        try:
            self.yearReturn = round(self.info['52WeekChange'], 2)
        except:
            self.yearReturn=0
        try:
            self.pegRatio = round(self.info['pegRatio'], 2)
        except:
            self.pegRatio=0
        self.shortPercentOfFloat = self.info['shortPercentOfFloat']
        self.marketCap = self.info['marketCap']
        try:
            self.payoutRatio = round(self.info['payoutRatio'], 2)
        except:
            self.payoutRatio=0
        try:
            self.fullTimeEmployees = self.info['fullTimeEmployees']
        except Exception as e:
            print(f'136: {e}')
            self.fullTimeEmployees = 0
        try:
            self.teps = round(self.info['trailingEps'], 2)
            self.longBusinesSummary = self.info['longBusinessSummary']
            self.industry = self.info['industry']
            try:
                self.profitMargins = round(self.info['profitMargins'], 2)
            except:
                self.profitMargins=0
            try:
                self.revenueGrowth = round(self.info['revenueGrowth'], 2)
            except:
                self.revenueGrowth=0
            try:

                self.grossMargins = round(self.info['grossMargins'], 2)
            except:
                self.grossMargins=0
            try:
                self.operatingCashflow = self.info['operatingCashflow']
            except:
                self.operatingCashflow=0
            self.ebitda = self.info['ebitda']
            try:
                self.operatingMargins = round(self.info['operatingMargins'], 2)
            except:
                self.operatingMargins=0


            self.bidSize = self.info['bidSize']
            self.dividendYield = round(self.info['dividendYield'], 2)
            try:

                self.fiftyTwoWeekLow = round(self.info['fiftyTwoWeekLow '], 2)
            except:
                self.fiftyTwoWeekLow = None
            self.operatingMargins = round(self.info['operatingMargins'], 2)
            self.logo = self.info['logo_url']

            self.grossMargins = self.info['grossMargins']
            self.freeCashflow = self.info['freeCashflow']
            self.targetMedianPrice = self.info['targetMedianPrice']
            self.currentPrice = round(self.info['currentPrice'], 2)

            self.fiveYearAvgDividendYield = self.info['fiveYearAvgDividendYield']
            self.fiftyTwoWeekHigh = round(self.info['fiftyTwoWeekHigh'], 2)
            self.averageVolume = self.info['averageVolume']
    
            try:
                self.trailingPE = round(self.info['trailingPE '], 2)
            except:
                self.trailingPE = None
            try:
                self.averageVolume10days = round(self.info['averageVolume10days'], 2)
            except:
                self.averageVolume10days=0
            try:
                self.trailingAnnualDividendRate = round(self.info['trailingAnnualDividendRate'], 2)
            except:
                self.trailingAnnualDividendRate=0

            self.sharesShortPriorMonth = self.info['sharesShortPriorMonth']
            try:
                self.twoHundredDayAverage = round(self.info['twoHundredDayAverage'], 2)
            except:
                self.twoHundredDayAverage=0
            try:

                self.priceToSalesTrailing12Months = round(self.info['priceToSalesTrailing12Months'], 2)
            except:
                self.priceToSalesTrailing12Months=0
            try:
                self.earningsQuarterlyGrowth = round(self.info['earningsQuarterlyGrowth'], 2)
            except:
                self.earningsQuarterlyGrowth=0
            self.lastSplitFactor = self.info['lastSplitFactor']
            self.enterpriseValue = self.info['enterpriseValue']

            self.dividendRate = round(self.info['dividendRate'], 2)
            self.fiftyDayAverage = round(self.info['fiftyDayAverage'], 2)
            self.mostRecentQuarter = self.info['mostRecentQuarter']
            self.enterpriseValue = self.info['netIncomeToCommon']
            try:
                self.recommendationMean = self.info['recommendationMean']
            except:
                self.recommendationMean=0
            self.totalCashPerShare = round(self.info['totalCashPerShare'], 2)
            self.totalRevenue = self.info['totalRevenue']
            self.enterpriseValue = self.info['revenuePerShare']

            self.sharesOutstanding = self.info['sharesOutstanding']
            self.enterpriseToEbitda = self.info['enterpriseToEbitda']
            self.enterpriseToRevenue = self.info['enterpriseToRevenue']
            self.revenuePerShare = self.info['revenuePerShare']
            try:
                self.feps = self.info['forwardEps']
            except:
                self.feps=0
            try:
                self.ebitdaMargins = self.info['ebitdaMargins']
            except:
                self.ebitdaMargins=0
            try:
                self.fpe = self.info['forwardPE']
            except:
                self.fpe=0
            try:
                self.logo = self.info['logo_url']
            except:
                self.logo='sss'

            self.response = requests.get(self.logo)
            self.img = Image.open(BytesIO(self.response.content))
            try:
                self.ptb = self.info['priceToBook']
            except:
                pass
            try:
                self.roe = self.info['returnOnEquity']
            except:
                pass
            self.currentRatio = self.info['currentRatio']
            self.debtEquityRatio = self.info['debtToEquity']
            self.insiders = self.info['heldPercentInsiders'] * 100
            self.tcps = self.info['totalCashPerShare']
            self.quickRatio = self.info['quickRatio']
            self.shortName = self.info['shortName']
        
            self.lastDividendValue = self.info['lastDividendValue']
            self.beta = self.info['beta']
            self.threeYearAverageReturn = self.info['threeYearAverageReturn']
            self.sharesPercentSharesOut = self.info['sharesPercentSharesOut'] * 100
        except Exception as e:
            print(f'err: {e}')
            self.mySave()

        self.method_list = [method for method in dir(self) if method.startswith('__') is False]
        self.mySave()

    def mySave(self):
        fp = os.path.join(dataDir, self.sector, self.symbol) + '.pickle'
        with open(fp, 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        x = json.dumps(self.__dict__, indent=4, sort_keys=True, default=str)
        j = json.loads(x)
        with open(self.filePath, 'w') as f:
            json.dump(j, f)

    def __repr__(self):
        return self.shortName


def updateUniverse():
    with open('universe.pickle', 'rb') as pickle_file:
        content = pickle.load(pickle_file)
    sc = []
    for c in content:
        sc.append(c.strip())
    final = set(sc)
    for s in final:
        print(s)
        x = Stock(s, '1y')


def sortUniverse():
    ml = ['payoutRatio', 'pegRatio', 'fullTimeEmployees', 'yearReturn', 'beta', 'currentRatio', 'debtEquityRatio',
          'ebitdaMargins', 'feps', 'fpe', 'insiders' 'ptb',
          'quickRatio', 'marketCap']
    for m in set(ml):
        try:
            temp(sortBy=m)
        except Exception as e:
            print(e)


def add_stock(symbol):
    #  r = requests.get(f'http://72.14.185.11/all/yearReturn/down').json()
    url = (f'http://72.14.185.11/all/marketCap/up')
    myobj = {"symbol": symbol}
    x = requests.post(url, data=myobj)


def sortStocks(sector, sortBy="marketCap", dir='up'):
    r = requests.get(f'http://72.14.185.11/{sector}/{sortBy}/{dir}').json()
    keys = []
    vals = []
    ranks = []
    pk=[]
    rank = 0
    for i in range(len(r)):
        val = r[i][sortBy]
        if val != None:
            rank += 1
            symbol = r[i]["symbol"]
            keys.append(symbol)
            ranks.append(rank)
            vals.append(val)
            pk.append(r[i]["pk"])

    dictionary = dict(zip(keys, vals))
    return dictionary


info = {
    "payoutRatio":
        "The payout ratio shows the proportion of earnings a company pays its shareholders in the form of dividends, expressed as a percentage of the company's total earnings. The calculation is derived by dividing the total dividends being paid out by the net income generated."}


sectorList = ['Basic%20Materials', 'Consumer%20Defensive', 'Healthcare', 'Communication%20Services', 'Energy',
              'Industrials',
              'Consumer%20Cyclical', 'Financial%20Services', 'Technology']


ml= ['zip', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'city', 'phone', 'state', 'country',
         'companyOfficers', 'website', 'maxAge', 'address1', 'industry', 'address2', 'ebitdaMargins', 'profitMargins',
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
         'fiveYearAvgDividendYield', 'fiftyTwoWeekLow', 'bid', 'tradeable', 'dividendYield', 'bidSize',
         'regularMarketPrice', 'preMarketPrice', 'logo_url']

ml2= ['fullTimeEmployees','ebitdaMargins', 'profitMargins',
         'grossMargins', 'operatingCashflow', 'revenueGrowth', 'operatingMargins', 'ebitda', 
          'grossProfits', 'freeCashflow',
         'currentRatio',
         'returnOnEquity', 'totalCash', 'totalRevenue', 'totalCashPerShare','revenuePerShare', 'quickRatio', 'enterpriseToRevenue',
        'enterpriseToEbitda','bookValue',"PriceToBook", 'floatShares', 'beta','enterpriseValue','trailingPE',
        'priceToSalesTrailing12Months',
         'pegRatio', 'ytdReturn', 'forwardPE', 'shortPercentOfFloat' 
          , 'payoutRatio',
         'dividendRate',  'marketCap']


def sortSectors(sortBy='marketCap', dir='up',normalize='True'):
    r = requests.get(f'http://72.14.185.11/sectors/{sortBy}/{dir}').json()
    print(f'len:{len(r)} r[0]:{r[0]["ave"]}')


    keys = []
    vals = []
    ranks = []
    rank = 0
    for i in range(len(r)):
        val=r[i]["ave"]
        sec=r[i]["name"]
        if val != None:
            rank += 1
            keys.append(sec)
            ranks.append(rank)
            vals.append(val)

    dictionary = dict(zip(keys, vals))
    return dictionary

sectorLL = ['Basic Materials', 'Consumer Defensive', 'Healthcare', 'Communication Services', 'Energy','Industrials','Consumer Cyclical', 'Financial Services', 'Technology']
sectorsDict=dict(zip(sectorList,sectorLL))
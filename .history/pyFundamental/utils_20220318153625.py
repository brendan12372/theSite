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
            pk.append(r[i]["id"])

    dictionary = dict(zip(keys,vals))
    return [dictionary,pk]


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




info = {
    "enterpriseToEbitda":" The EV/EBITDA ratio is a popular metric used as a valuation tool to compare the value of a company, debt included, to the companys cash earnings less non-cash expenses. It's ideal for analysts and investors looking to compare companies within the same industry."
"The enterprise-value-to-EBITDA ratio is calculated by dividing EV by EBITDA or earnings before interest, taxes, depreciation, and amortization. Typically, EV/EBITDA values below 10 are seen as healthy. However, the comparison of relative values among companies within the same industry is the best way for investors to determine companies with the healthiest EV/EBITDA within a specific sector. ",
    "payoutRatio":
        "The payout ratio shows the proportion of earnings a company pays its shareholders in the form of dividends,"
        " expressed as a percentage of the company's total earnings. The calculation is derived by dividing the "
        "total dividends being paid out by the net income generated.",
"ebitdaMargins":"The EBITDA margin is a measure of a company's operating profit as a percentage of its revenue. The "
                "acronym EBITDA stands for earnings before interest, taxes, depreciation, and amortization. Knowing "
                "the EBITDA margin allows for a comparison of one company's real performance to others in its "
                "industry.",

"marketCap":"Market cap—or market capitalization—refers to the total value of all a company's shares of stock. It is calculated by multiplying the price of a stock by its total number of outstanding shares. For example, a company with 20 million shares selling at $50 a share would have a market cap of $1 billion.",
"PriceToBook": "Companies use the price-to-book ratio (P/B ratio) to compare a firm's market capitalization to its book value. It's calculated by dividing the company's stock price per share by its book value per share (BVPS). An asset's book value is equal to its carrying value on the balance sheet, and companies calculate it netting the asset against its accumulated depreciation. Book value is also the tangible net asset value of a company calculated as total assets minus intangible assets (.e.g. patents, goodwill) and liabilities. For the initial outlay of an investment, book value may be net or gross of expenses, such as trading costs, sales taxes, and service charges. Some people may know this ratio by its less common name, the price-equity ratio.",
"fullTimeEmployees": "Full-Time Employees means Employees with regularly scheduled and budgeted Working Hours of no less than forty (40) hours per week.",
"pegRatio":"The price/earnings to growth ratio (PEG ratio) is a stock's price-to-earnings (P/E) ratio divided by the growth rate of its earnings for a specified time period. The PEG ratio is used to determine a stock's value while also factoring in the company's expected earnings growth, and it is thought to provide a more complete picture than the more standard P/E ratio. ",
"yearReturn":"change in share price last year",
"fpe":"A variation of the price-to-earnings ratio (P/E ratio) is the forward P/E ratio, which is based on a prediction of a company's future earnings. Earnings used in the forward P/E ratio are estimates of future earnings, while the standard P/E ratio uses actual earnings per share from the company's previous four quarters.",
"quickRatio":" QR = (Current Assets - Inventories - Prepaid Expenses) / Current Liabilities.The quick ratio is an indicator of a company’s short-term liquidity position and measures a company’s ability to meet its short-term obligations with its most liquid assets. Since it indicates the company’s ability to instantly use its near-cash assets (assets that can be converted quickly to cash) to pay down its current liabilities, it is also called the acid test ratio. An 'acid test' is a slang term for a quick test designed to produce instant results. ",
"currentRatio":" The current ratio is a liquidity ratio that measures a company’s ability to pay short-term obligations or those due within one year. It tells investors and analysts how a company can maximize the current assets on its balance sheet to satisfy its current debt and other payables.A current ratio that is in line with the industry average or slightly higher is generally considered acceptable. A current ratio that is lower than the industry average may indicate a higher risk of distress or default. Similarly, if a company has a very high current ratio compared with its peer group, it indicates that management may not be using its assets efficiently.The current ratio is called current because, unlike some other liquidity ratios, it incorporates all current assets and current liabilities. The current ratio is sometimes called the working capital ratio. ",
"returnOnEquity":"Return on equity (ROE) is a measure of financial performance calculated by dividing net income by shareholders' equity. Because shareholders' equity is equal to a company’s assets minus its debt, ROE is considered the return on net assets. ROE is considered a gauge of a corporation's profitability and how efficient it is in generating profits. ",
    "teps":
        " Trailing earnings per share (EPS) is a company's earnings generated over a prior period (often a fiscal year) reported on a per-share basis."
"The term trailing moreover implies a value calculated on a rolling basis. That is, trailing EPS may describe the most recent 12-month period or four earnings releases. The period used for a trailing EPS will change as the most recent earnings are added to the calculation and earnings from five quarters ago are dropped from the calculation. ",
    "feps":"The Forward Price-to-Earnings or Forward P/E Ratio. The forward P/E ratio (or forward price-to-earnings ratio) divides the current share price of a company by the estimated future earnings per share (EPS) of that company.",
    "debtEquityRatio":"The debt-to-equity (D/E) ratio compares a company's total liabilities to its shareholder equity and can be used to evaluate how much leverage a company is using. Higher-leverage ratios tend to indicate a company or stock with higher risk to shareholders.",
    "shortPercentOfFloat":"The short percentage of float is the percentage of a company's stock that has been shorted by institutional traders, compared to the number of shares of a company's stock that are available to the public.",
    "beta":"Beta is a measure of a stock's volatility in relation to the overall market. By definition, the market, such as the S&P 500 Index, has a beta of 1.0, and individual stocks are ranked according to how much they deviate from the market. A stock that swings more than the market over time has a beta above 1.0.",
    "insiders":"The insiders percentage is the percentage of float is the percentage of a company's stock that has been shorted by institutional traders,ort percentage of float is owned by employees",
    "enterpriseValue":"Enterprise value (EV) is a measure of a company's total value, often used as a more comprehensive alternative to equity market capitalization. EV includes in its calculation the market capitalization of a company but also short-term and long-term debt as well as any cash on the company's balance sheet. Enterprise value is a popular metric used to value a company for a potential takeover. ",
    
    
    "dividendYield":" The dividend yield, expressed as a percentage, is a financial ratio (dividend/price) that shows how much a company pays out in dividends each year relative to its stock price."
"The reciprocal of the dividend yield is the price/dividend ratio. ",

"bookValue":" Book value is equal to the cost of carrying an asset on a company's balance sheet, and firms calculate it netting the asset against its accumulated depreciation. As a result, book value can also be thought of as the net asset value (NAV) of a company, calculated as its total assets minus intangible assets (patents, goodwill) and liabilities. For the initial outlay of an investment, book value may be net or gross of expenses such as trading costs, sales taxes, service charges, and so on."

"The formula for calculating book value per share is the total common stockholders' equity less the preferred stock, divided by the number of common shares of the company. " ,

"forwardPE":"Forward price-to-earnings (forward P/E) is a version of the ratio of price-to-earnings (P/E) that uses forecasted earnings for the P/E calculation. While the earnings used in this formula are just an estimate and not as reliable as current or historical earnings data, there are still benefits to estimated P/E analysis. ",
'trailingPE':" Trailing price-to-earnings (P/E) is a relative valuation multiple that is based on the last 12 months of actual earnings. It is calculated by taking the current stock price and dividing it by the trailing earnings per share (EPS) for the past 12 months."

"Trailing P/E can be contrasted with the forward P/E, which instead uses projected future earnings to calculate the price-to-earnings ratio.  ",
"profitMargins":" Profit margin is one of the commonly used profitability ratios to gauge the degree to which a company or a business activity makes money. It represents what percentage of sales has turned into profits. Simply put, the percentage figure indicates how many cents of profit the business has generated for each dollar of sale. For instance, if a business reports that it achieved a 35% profit margin during the last quarter, it means that it had a net income of $0.35 for each dollar of sales generated."

"There are several types of profit margin. In everyday use, however, it usually refers to net profit margin, a company’s bottom line after all other expenses, including taxes and one-off oddities, have been taken out of revenue. ",
"grossMargins":"Gross margin is net sales less the cost of goods sold (COGS). In other words, it's the amount of money a company retains after incurring the direct costs associated with producing the goods it sells and the services it provides. The higher the gross margin, the more capital a company retains, which it can then use to pay other costs or satisfy debt obligations. The net sales figure is gross revenue, less the returns, allowances, and discounts. ",
"operatingCashflow":"Operating cash flow (OCF) is a measure of the amount of cash generated by a company's normal business operations. Operating cash flow indicates whether a company can generate sufficient positive cash flow to maintain and grow its operations, otherwise, it may require external financing for capital expansion. ",
"revenueGrowth":"Quarterly revenue growth is an increase in a company's sales in one quarter compared to sales of a different quarter. The current quarter's sales figure can be compared on a year-over-year basis (e.g., 3Q sales of Year 1 compared with 3Q sales of Year 2) or sequentially (3Q sales of Year 1 compared with 4Q sales of Year 1). This gives analysts, investors, and additional stakeholders an idea of how much a company's sales are increasing over time. ",
"ebitda":" EBITDA, or earnings before interest, taxes, depreciation, and amortization, is a measure of a company’s overall financial performance and is used as an alternative to net income in some circumstances. EBITDA, however, can be misleading because it strips out the cost of capital investments like property, plants, and equipment."

"This metric also excludes expenses associated with debt by adding back interest expense and taxes to earnings. Nonetheless, it is a more precise measure of corporate performance since it is able to show earnings before the influence of accounting and financial deductions."

"Simply put, EBITDA is a measure of profitability. While there is no legal requirement for companies to disclose their EBITDA, according to U.S. generally accepted accounting principles (GAAP), it can be worked out and reported using the information found in a company’s financial statements."

"The earnings, tax, and interest figures are found on the income statement, while the depreciation and amortization figures are normally found in the notes to operating profit or on the cash flow statement. The usual shortcut to calculate EBITDA is to start with operating profit, also called earnings before interest and tax (EBIT), then add back depreciation and amortization. ",
"grossProfits":"Gross profit is the profit a company makes after deducting the costs associated with making and selling its products, or the costs associated with providing its services. Gross profit will appear on a company's income statement and can be calculated by subtracting the cost of goods sold (COGS) from revenue (sales). These figures can be found on a company's income statement. Gross profit may also be referred to as sales profit or gross income. ",
"operatingMargins":"The operating margin measures how much profit a company makes on a dollar of sales after paying for variable costs of production, such as wages and raw materials, but before paying interest or tax. It is calculated by dividing a company’s operating income by its net sales. Higher ratios are generally better, illustrating the company is efficient in its operations and is good at turning sales into profits.",
"trailingAnnualDividendRate":"Trailing dividend yield gives the dividend percentage paid over a prior period, typically one year. A trailing twelve month dividend yield, denoted as TTM, includes all dividends paid during the past year in order to calculate the dividend yield.",
"dividendRate":"The dividend rate is the total expected dividend payments from an investment, fund or portfolio expressed on an annualized basis plus any additional non-recurring dividends that an investor may receive during that period. Depending on the company's preferences and strategy, the dividend rate can be fixed or adjustable."

"Dividend rate is closely related to dividend yield, and sometimes used interchangeably. ",


"priceToSalesTrailing12Months":"The price-to-sales ratio (Price/Sales or P/S) is calculated by taking a company's market capitalization (the number of outstanding shares multiplied by the share price) and divide it by the company's total sales or revenue over the past 12 months.1"

"The lower the P/S ratio, the more attractive the investment. Price-to-sales provides a useful measure for sizing up stocks. ",
"floatShares":" Floating stock is the number of shares available for trading of a particular stock. Low float stocks are those with a low number of shares. Floating stock is calculated by subtracting closely-held shares and restricted stock from a firm’s total outstanding shares."

"Closely-held shares are those owned by insiders, major shareholders, and employees. Restricted stock refers to insider shares that cannot be traded because of a temporary restriction, such as the lock-up period after an initial public offering (IPO)."

"A stock with a small float will generally be more volatile than a stock with a large float. This is because, with fewer shares available, it may be harder to find a buyer or seller. This results in larger spreads and often lower volume. ",
"enterpriseToRevenue":"The enterprise value-to-revenue multiple (EV/R) is a measure of the value of a stock that compares a company's enterprise value to its revenue. EV/R is one of several fundamental indicators that investors use to determine whether a stock is priced fairly. The EV/R multiple is also often used to determine a company's valuation in the case of a potential acquisition. It’s also called the enterprise value-to-sales multiple. ",
"freeCashflow":" Free cash flow (FCF) is the cash a company generates after taking into consideration cash outflows that support its operations and maintain its capital assets. In other words, free cash flow is the cash left over after a company pays for its operating expenses and capital expenditures (CapEx)."

"FCF is the money that remains after paying for items such as payroll, rent, and taxes, and a company can use it as it pleases. Knowing how to calculate free cash flow and analyze it will help a company with its cash management. FCF calculation will also provide investors with insight into a company's financials, helping them make better investment decisions."

"Free cash flow is an important measurement since it shows how efficient a company is at generating cash. Investors use free cash flow to measure whether a company might have enough cash for dividends or share buybacks. In addition, the more free cash flow a company has, the better it is placed to pay down debt and pursue opportunities that can enhance its business, making it an attractive choice for investors."

"This article will cover how a company calculates free cash flow and how to interpret that free cash flow number to choose good investments that will generate a return on your capital. ",


"totalCashPerShare": "Cash per share (CPS) measures how much cash a company has on hand on a per-share basis. It can also be expressed as a financial ratio that can be calculated by tallying up a companys total cash on its balance sheet, including easy to liquidate short-term investments, and then dividing that figure by the number of shares outstanding."

"The cash per share indicates the amount of a company’s share price that's immediately available for spending on activities such as research and development (R&D), mergers and acquisitions (M&A), purchasing or improving assets, paying down debt, buying back shares, and making dividend payments to shareholders, etc. "
}
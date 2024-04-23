from clearData.replace1By10 import replace1by10
from charts.chart import plot
from indicators.movingAverage import sma
from clearData.unite import unite
from strategies.SMAStrategy import smaMarketTiming
from strategies.momentumStrategies import calculateAccMom, accMomStrategy, accDualMomStrategy
from otherFunctions.addDividends import addDividends
from clearData.clearDataSP500 import clearData
from metrics.annualizedReturn import annualizedReturn
from clearData.clearDataBonds import clearDataBonds


SP500_source = r'C:\Users\l.elizalde\OneDrive - ESTIA\Divers\python\trading_strategy\sources\investment\SP500_monthly_1871-2018.csv'
bonds_source = r'C:\Users\l.elizalde\OneDrive - ESTIA\Divers\python\trading_strategy\sources\investment\bonds_price_approximation_1871-2022.csv'


SP500Data = replace1by10(SP500_source)

date, price, dividends = clearData(SP500Data)
price = unite(price)

dividendsAdded = addDividends(date, price, dividends)


bondPrice = clearDataBonds(bonds_source)


accDualMomStrategyPrice = accDualMomStrategy(price, bondPrice, reinvestDividends=True, dividends=dividends, date=date)
#print(annualizedReturn(accDualMomStrategyPrice))


#accMomStrategyPrice = accMomStrategy(price, buyEnable=True, sellEnable=True, reinvestDividends=True, dividends=dividends, date=date)
#print(annualizedReturn(accMomStrategyPrice))


smaMT = smaMarketTiming(price, 10, reinvestDividends=True, dividends=dividends, date=date, buyEnable=True, sellEnable=False)

print(smaMT)

series = [0 for x in range(4)]
series[0] = price
series[1] = dividendsAdded
series[2] = smaMT
series[3] = accDualMomStrategyPrice
#series[4] = accMomStrategyPrice

plot(date, series, 'Strategy tester', logEnable=False)


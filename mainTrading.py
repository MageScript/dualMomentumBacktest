from strategies.momentumStrategies import calculateAccMom, generateArrayOfOrderDecisionFromAccMomScores, accMomStrategy
from clearData.clearDataTrading import clearDataTrading
from clearData.unite import unite
from charts.chart import plot
from indicators.movingAverage import sma
from strategies.SMAStrategy import smaMarketTiming
from metrics.standardDeviation import standardDeviation
from metrics.totalReturn import totalReturn

date, instrumentPrice = clearDataTrading(r"C:\Users\Megaport\OneDrive - ESTIA\Divers\python\trading_strategy\sources\trading\DAT_MT_EURUSD_M1_2021.csv")
instrumentPrice = unite(instrumentPrice)

#accMomStrategy = accMomStrategy(instrumentPrice, period='daily', buyEnable=True, sellEnable=False, dividends=False)

SMA = sma(instrumentPrice, 50)

SMAstrategy = smaMarketTiming(instrumentPrice, 50, reinvestDividends=False, buyEnable=True, sellEnable=True)


series = [0 for x in range(3)]
series[0] = instrumentPrice
#series[1] = accMomStrategy
series[1] = SMA
series[2] = SMAstrategy

stdDev = standardDeviation(SMAstrategy)
ttlReturn = totalReturn(SMAstrategy)

print(stdDev, ' ', ttlReturn)

plot(date, series, 'BTC acc mom', logEnable=False)
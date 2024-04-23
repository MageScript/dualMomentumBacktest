def totalReturn(price):

    ttlReturn = ((price[len(price)-1] / price[0]) - 1) * 100

    return ttlReturn
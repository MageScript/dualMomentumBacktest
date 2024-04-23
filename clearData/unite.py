def unite(price):
    firstPrice = price[0]
    for index, pr in enumerate(price):
        price[index] = pr / firstPrice
    return price
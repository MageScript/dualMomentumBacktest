from cmath import log
import matplotlib.pyplot as plt

def plot(date, series, title, logEnable=None):

    
    for srs in series:
        plt.plot(date, srs, label = "AAA")


    plt.xlabel('time (month)')
    plt.ylabel('price (usd)')
    plt.title(title)

    if logEnable == True:
        plt.yscale('log')


    plt.legend()
    plt.show()



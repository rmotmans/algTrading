import algTrading.trend.trend_ind as trend

"""
function RSI (Relative strength index)
    input:  - data array
            - moving average length

    output: -array of same length as data array, but with RSI
"""
def RSI(data, period = 14):
    U = [0.0000001]
    D = [0.0000001]
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff >= 0:
            U.append(diff)
            D.append(0.0000001)
        else:
            U.append(0.0000001)
            D.append(-diff)
    
    SMMA_U = trend.SMMA(U, period)
    SMMA_D = trend.SMMA(D, period)

    RS = [x/y for (x,y) in zip(SMMA_U, SMMA_D)]
    RSI = [(100-100/(1+x)) for x in RS]

    return RSI

    

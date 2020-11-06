from statistics import mean, stdev


"""
function moving_average
    input:  - data array
            - moving average length

    output: -array of same length as data array, but with moving average
"""
def moving_average(data, period):
    result = []
    for i in range(len(data)):
        if i < period-1:
            result.append(mean(data[0:i+1]))
        else:
            result.append(mean(data[i-period+1:i+1]))
            
    return result

"""
function moving_standard_deviation
    input:  - data array
            - moving standard deviation length

    output: -array of same length as data array, but with moving standard deviation
"""
def moving_standard_deviation(data, period):
    result = [0]
    for i in range(len(data)-1):
        if i < period - 2:
            result.append(stdev(data[0:i+2]))
        else:
            result.append(stdev(data[i-period+2:i+2]))
            
    return result

"""
function bollinger_bands
    input:  - data array
            - moving length
            - band factor

    output: - Moving average
            - 2 arrays of same length as data array, but with bollinger bands (upper bollinger band, lower bollinger band)
"""
def bollinger_bands(data, period, bf):
    MA = moving_average(data, period)
    SDEV = moving_standard_deviation(data, period)

    upper_bollinger_band = [x + bf*y for (x,y) in zip(MA, SDEV)]
    lower_bollinger_band = [x - bf*y for (x,y) in zip(MA, SDEV)]

    return MA, upper_bollinger_band, lower_bollinger_band

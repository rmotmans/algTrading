from statistics import mean, stdev


"""
function moving_average
    input:  - data array
            - moving average length

    output: -array of same length as data array, but with moving average
"""
def moving_average(data, length):
    result = []
    for i in range(len(data)):
        if i < length-1:
            result.append(mean(data[0:i+1]))
        else:
            result.append(mean(data[i-length+1:i+1]))
            
    return result

"""
function moving_standard_deviation
    input:  - data array
            - moving standard deviation length

    output: -array of same length as data array, but with moving standard deviation
"""
def moving_standard_deviation(data, length):
    result = [0]
    for i in range(len(data)-1):
        if i < length - 2:
            result.append(stdev(data[0:i+2]))
        else:
            result.append(stdev(data[i-length+2:i+2]))
            
    return result

"""
function bollinger_bands
    input:  - data array
            - moving length
            - band factor

    output: -2 arrays of same length as data array, but with bollinger bands (upper bollinger band, lower bollinger band)
"""
def bollinger_bands(data, length, bf):
    MA = moving_average(data, length)
    SDEV = moving_standard_deviation(data, length)

    upper_bollinger_band = [x + bf*y for (x,y) in zip(MA, SDEV)]
    lower_bollinger_band = [x - bf*y for (x,y) in zip(MA, SDEV)]

    return upper_bollinger_band, lower_bollinger_band

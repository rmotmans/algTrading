from statistics import mean

"""
function moving_average
    input:  - data array
            - moving average length

    output: -array of same length as data array, but with moving average
"""

def moving_average(data, length):
    result = []
    for i in range(len(data)):
        if i < length:
            result.append(mean(data[0:i+1]))
        else:
            result.append(mean(data[i-length+1:i+1]))
            
    return result
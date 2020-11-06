

def RSI(data, period):
    U = [0]
    D = [0]
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff >= 0:
            U.append(diff)
            D.append(0)
        else:
            U.append(0)
            D.append(-diff)
    
    

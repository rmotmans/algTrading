import algTrading.momentum.momentum_ind as mo 
import algTrading.trend.trend_ind as trend

print('test test')

test_array = [1,2,3,4,5,6,7,8,9,4,5,8,7,4,5,2,2,1,4,5,8]
result1 = mo.RSI(test_array,8)

for i in range(len(result1)):
    print(i+1, result1[i])

import algTrading.momentum.momentum_ind as mo 
import algTrading.trend.trend_ind as trend

print('test test')

test_array = [1,2,3,4,5,6,7,8,9,4,5,8,7,4,5,2,2,1,4,5,8]
result3, result1, result2 = trend.bollinger_bands(test_array,3, 1)
#result3 = trend.moving_average(test_array,3)

for i in range(len(result1)):
    print(i+1,result2[i], result3[i], result1[i])

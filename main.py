from chart import showCharts
import matplotlib.pyplot as plt
import random

searchValue = [random.randint(1, 10000) for _ in range(10000)]
arrayNumber = list(range(1,10001))

xaxis = []
yaxis = []
runChart = showCharts()

def searchAlgo(num, searchFor):
    iteration = 1
    for numArrayTicks in num:
        if searchFor == numArrayTicks:
            break
        else:
            iteration += 1
    return iteration

for indexX, value in enumerate(searchValue):
    xaxis.append(searchAlgo(arrayNumber, searchValue[indexX]))
    
runChart.lineChart(xaxis,arrayNumber)





    
    
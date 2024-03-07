from chart import showCharts
import matplotlib.pyplot as plt
import random

searchValues = []
iterationValuesLinear = []
iterationValuesBinary = []
arrayNumber = list(range(1,101))


def searchAlgo(num, searchFor):
    loopValues = []
    for search in searchFor:
        iteration = 0
        for ticks in num:
            if search == ticks:
                break
            else:
                iteration += 1
        loopValues.append(iteration)
    return loopValues

def binarySearch(num, searchFor):
    loopValuesBinary = []
    for search in searchFor:
        left = 0
        right = 99
        midpoint = (right+left)//2
        repeat = 1
        iteration = 0
        while(repeat):
            if (search == num[midpoint]) or (right < left) or (right == left):
                repeat = 0
                break
            elif search > num[midpoint]:
                #print("search > "+str(search)+" : "+str(left)+" : "+str(right)+" : "+str(midpoint)+" : "+str(num[midpoint]))
                left = midpoint + 1
                iteration += 1
                midpoint = (right+left)//2
            elif search < num[midpoint]:
                #print("search < "+str(search)+" : "+str(left)+" : "+str(right)+" : "+str(midpoint)+" : "+str(num[midpoint]))
                right = midpoint - 1
                iteration += 1
                midpoint = (right+left)//2
        loopValuesBinary.append(iteration)
    return loopValuesBinary

inputDigit = int(input("Enter max digit #: "))
searchValues.append([random.randint(1, inputDigit) for _ in range(100)])
iterationValuesLinear.append(searchAlgo(arrayNumber, searchValues[0]))
iterationValuesBinary.append(binarySearch(arrayNumber, searchValues[0]))

showCharts.plotChart(iterationValuesLinear[0],
                     iterationValuesBinary[0],
                     arrayNumber)







    
    
import matplotlib.pyplot as plt

class showCharts:
    def lineChart(self, length, iteration):
        x = length
        y = iteration
        plt.plot(x,y)
        plt.title = "Search Algo Chart"
        plt.xlabel = "Number of Elements"
        plt.ylabel = "Number of Iterations"
        plt.show()
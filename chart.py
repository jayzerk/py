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
        
    def plotChart(length1, length2, length3,
                  length4, length5, length6,
                  iteration):
        plt.xlim(0, 100)
        plt.subplot(1,3,1)
        plt.scatter(length1, iteration, color='red', alpha=0.4)
        
        plt.subplot(1,3,2)
        plt.scatter(length2, iteration, color='red', alpha=0.4)

        plt.subplot(1,3,3)
        plt.scatter(length3, iteration, color='red', alpha=0.4)
        
        plt.subplot(2,3,1)
        plt.scatter(length4, iteration, color='blue', alpha=0.4)
        
        plt.subplot(2,3,2)
        plt.scatter(length5, iteration, color='blue', alpha=0.4)
        
        plt.subplot(2,3,3)
        plt.scatter(length6, iteration, color='blue', alpha=0.4)
        plt.tight_layout()
        plt.show()
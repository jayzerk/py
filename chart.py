import matplotlib.pyplot as plt

class showCharts:
        
    def plotChart(length1, length2, iteration):
        
        plt.subplot(1,2,1)
        plt.scatter(length1, iteration, color='red', alpha=0.4)
        plt.xlim(0, 100)
        plt.ylim(0, max(iteration))
        
        
        plt.subplot(1,2,2)
        plt.scatter(length2, iteration, color='red', alpha=0.4)
        plt.xlim(0, 100)
        plt.ylim(0, max(iteration))


        plt.tight_layout()
        plt.show()
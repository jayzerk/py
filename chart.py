import matplotlib.pyplot as plt

class showCharts:
        
    def plotChart(iter_linear, iter_binary, arrayLength):
        highest_value, hv_count =showCharts.checkWorstCase(iter_linear)
        plt.subplot(1,2,1)
        plt.scatter(iter_linear, arrayLength, color='red', alpha=0.4)
        plt.ylim(0, max(arrayLength))
        plt.text(0.5, 1.05,
                'Worst Case: {}'.format(highest_value)+' from {}'.format(max(arrayLength)),
                ha='center', transform=plt.gca().transAxes)
        plt.text(.5, 1.01,
                'Worst Case Count: {}'.format(hv_count)+' out of {}'.format(max(arrayLength)),
                ha='center', transform=plt.gca().transAxes)
        highest_value, hv_count =showCharts.checkWorstCase(iter_binary)
        
        plt.subplot(1,2,2)
        plt.scatter(iter_binary, arrayLength, color='red', alpha=0.4)
        plt.ylim(0, max(arrayLength))
        plt.text(0.5, 1.05,
                'Worst Case: {}'.format(highest_value)+' from {}'.format(max(arrayLength)),
                ha='center', transform=plt.gca().transAxes)
        plt.text(0.5, 1.01,
                'Worst Case Count: {}'.format(hv_count)+' out of {}'.format(max(arrayLength)),
                ha='center', transform=plt.gca().transAxes)

        plt.tight_layout()
        plt.show()
        
    def checkWorstCase(iter_list):
        highest_value = max(iter_list)
        hv_count = iter_list.count(highest_value)
        return [highest_value, hv_count]
    

        
import numpy as np
import matplotlib.pyplot as plt

from constants.colors import colors

def ganttPlot(self):
    
    self.canvas.gnt.set_ylim(0, 50)
    self.canvas.gnt.set_xlim(0, self.flowShopSchedule.makespan + self.flowShopSchedule.makespan//10)
    self.canvas.gnt.set_xlabel('')
    self.canvas.gnt.set_ylabel('Machines')

    labels = []
    y_ticks = []
    
    for i in range(len(self.flowShopSchedule.timeMatrix)):
            labels.append('M' + str(i+1))
            y_ticks.append(15 + i * 10)
    labels.reverse()

    self.canvas.gnt.set_yticks(y_ticks)
    self.canvas.gnt.set_yticklabels(labels)


    for i in range(0, len(self.flowShopSchedule.timeMatrix)):
            data = [(self.flowShopSchedule.timeMatrixStart[i][j], self.flowShopSchedule.timeMatrix[i][j]-self.flowShopSchedule.timeMatrixStart[i][j]) for j in range(len(self.flowShopSchedule.timeMatrix[0]))]
            self.canvas.gnt.broken_barh(data, (10 * len(self.flowShopSchedule.timeMatrix) - 10 * i + 2.5, 5), color=colors)

    minor_ticks = np.arange(0, self.flowShopSchedule.makespan + 5, 1)

    if self.gridValue:
            self.ax = plt.gca()
            self.ax.set_xticks(minor_ticks, minor=True)

            self.ax.grid(True, axis='x',which="major", alpha=0.2, color='#373B54')
            self.ax.grid(True, axis='x',which="minor", alpha=0.1, color='#373B54')

    self.canvas.draw()
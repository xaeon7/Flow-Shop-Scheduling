from constants.colors import colors

def barPlot(self, data):
        machines = []
        for i in range(len(data)):
                machines.append('M' + str(i+1))

        self.canvas.gnt.bar(machines,data, color = colors)

        for index, value in enumerate(data):
                self.canvas.gnt.text(index, value, str(value)[:6], ha= 'center', va='bottom', color = colors[index])
                
        self.canvas.draw()
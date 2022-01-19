from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from functions.plots.MatplotlibCanvas import MatplotlibCanvas
import matplotlib.pyplot as plt
import sip

from constants.plots import plots

def initializePlot(self, plot):
    
    plt.clf()
    
    try:
        if plot == plots["TFR"]:
            self.tfrTB.removeWidget(self.toolbar)
            self.plotTFR.removeWidget(self.canvas)
            
        elif plot == plots["TAP"]:
            self.tapTB.removeWidget(self.toolbar)
            self.plotTAP.removeWidget(self.canvas)
        
        elif plot == plots["TAR"]:
            self.tarTB.removeWidget(self.toolbar)
            self.plotTAR.removeWidget(self.canvas)
        
        elif plot == plots["Gantt"]:
            self.ganttTB.removeWidget(self.toolbar)
            self.plotGANTT.removeWidget(self.canvas)
        
        sip.delete(self.toolbar)
        sip.delete(self.canvas)
        self.toolbar = None
        self.canvas = None

    except Exception as e:
        print(e)
        pass

    self.canvas = MatplotlibCanvas(self)
    self.toolbar = NavigationToolbar2QT(self.canvas, self.centralwidget)
    
    if plot == plots["TFR"]:
        self.tfrTB.addWidget(self.toolbar)
        self.plotTFR.addWidget(self.canvas)
        
    elif plot == plots["TAP"]:
        self.tapTB.addWidget(self.toolbar)
        self.plotTAP.addWidget(self.canvas)
    
    elif plot == plots["TAR"]:
        self.tarTB.addWidget(self.toolbar)
        self.plotTAR.addWidget(self.canvas)
    
    elif plot == plots["Gantt"]:
        self.ganttTB.addWidget(self.toolbar)
        self.plotGANTT.addWidget(self.canvas)
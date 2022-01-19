from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

import matplotlib

from functions.plots.ganttPlot import ganttPlot

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


from lib.CDS import FlowShopSchedule

from functions.plots.MatplotlibCanvas import MatplotlibCanvas
from functions.plots.setAlgorithm import setAlgorithm
from functions.plots.barPlot import barPlot
from functions.plots.ganttPlot import ganttPlot
from functions.plots.initializePlot import initializePlot

import functions.buttons.navigation as navigation
from functions.buttons.plotsNavigation import plotsNavigation

import styles.styles as styles

from constants.colors import colors
from constants.plots import plots

class DisplayGantt(QMainWindow):
        
    def __init__(self, widget):
        super(DisplayGantt, self).__init__()
        
        #? load UI file
        loadUi("src/screens/ui/PlotsScreen.ui",self)

        #? Initialize the results
        self.flowShopSchedule = FlowShopSchedule(widget.jobsMatrix)

        #? Set the algorithm
        setAlgorithm(self, widget = widget)
        
        #? handle navigation
        navigation.handlePlotsScreenNavigation(self, widget = widget)

        #? Grid state
        self.gridValue = False

        #? check if TAP is available
        if not len(self.flowShopSchedule.stopPreparationRate):
            self.tap.setEnabled(False)
            self.tap.setStyleSheet(styles.graphTypeButtonDisabled)
        else:
                self.tap.setEnabled(True)
                self.tap.setStyleSheet(styles.graphTypeButtonEnabled)


        #? Initialize graphs
        self.canvas = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canvas, self.centralwidget)
        self.tarTB.addWidget(self.toolbar)
        self.tfrTB.addWidget(self.toolbar)
        self.tapTB.addWidget(self.toolbar)
        self.ganttTB.addWidget(self.toolbar)
        self.displayGantt()


        #? Graphs navigation
        self.gantt.clicked.connect(self.displayGantt)
        self.tfr.clicked.connect(self.displayTFR)
        self.tap.clicked.connect(self.displayTAP)
        self.tar.clicked.connect(self.displayTAR)
        self.checkBox.clicked.connect(self.displayGrid)


        #? Display data 
        Sequence = ', '.join([str(elem) for elem in self.flowShopSchedule.sequence])
        self.sigma.setText(Sequence)
        self.c_max.setText(str(self.flowShopSchedule.makespan))
        self.tt.setText(str(self.flowShopSchedule.totalTardiness))


    def displayTFR(self):
        
        #? navigate to the graph
        self.plots.setCurrentWidget(self.tfrPlot)
        
        #? handle graph buttons state
        plotsNavigation(self, plot = plots["TFR"])

        #? Initialize Plot
        initializePlot(self, plot = plots["TFR"])
        
        #? plot the data
        data = self.flowShopSchedule.operatingRate
        barPlot(self, data)
                

    def displayTAP(self):
        self.plots.setCurrentWidget(self.tapPlot)

        #? handle graph buttons state
        plotsNavigation(self, plot = plots["TAP"])

        #? Initialize Plot
        initializePlot(self, plot = plots["TAP"])

        #? plot the data
        data = self.flowShopSchedule.stopPreparationRate
        barPlot(self, data)



    def displayTAR(self):
        
        #? navigate to the graph
        self.plots.setCurrentWidget(self.tarPlot)

        #? handle graph buttons state
        plotsNavigation(self, plot = plots["TAR"])
        
        #? Initialize Plot
        initializePlot(self, plot = plots["TAR"])
        
        #? plot the data
        data = self.flowShopSchedule.stopRate
        barPlot(self, data)


    def displayGrid(self):
            self.gridValue = not self.gridValue
            self.displayGantt()


    def displayGantt(self):
        #? navigate to the graph
        self.plots.setCurrentWidget(self.ganttPlot)

        #? handle graph buttons state
        plotsNavigation(self, plot = plots["Gantt"])
        
        #? Initialize Plot
        initializePlot(self, plot = plots["Gantt"])
        
        #? plot the data       
        ganttPlot(self)
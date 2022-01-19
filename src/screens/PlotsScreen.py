from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

import numpy as np
import sip

from lib.CDS import FlowShopSchedule

from functions.plots.MatplotlibCanvas import MatplotlibCanvas

colors = ['#FEB800', '#33D6A0', '#6F52ED', '#FE4C61', '#06A6FF', '#FF7A01', '#FF66B3', '#4DD1BA', '#FA656A', '#477CFF']


class DisplayGantt(QMainWindow):
    def __init__(self, widget):
        super(DisplayGantt, self).__init__()
        loadUi("src/screens/ui/PlotsScreen.ui",self)

        self.flowShopSchedule = FlowShopSchedule(widget.jobsMatrix)
        self.logo.clicked.connect(self.goHome)


        if not widget.delay and not widget.prep:
            self.flowShopSchedule.CDS()

        elif widget.delay and not widget.prep:
            self.flowShopSchedule.Delay(widget.delaySeq, widget.optimize)

        elif not widget.delay and widget.prep:
            self.flowShopSchedule.Preparation(widget.prepMatrix, widget.algo)

        elif widget.delay and widget.prep:
            self.flowShopSchedule.PreparationAndDelay(widget.prepMatrix, widget.delaySeq, widget.algo)

        self.gridValue = False

###########????????????????
        if not len(self.flowShopSchedule.stopPreparationRate):
            self.tap.setEnabled(False)
            self.tap.setStyleSheet("color: \"#ffffff\";\n"
        "background-color: rgb(181, 181, 204);\n"
        "border: 1px solid rgb(181, 181, 204) ;\n"
        "border-top-left-radius:\'5px\';\n"
        "border-bottom-left-radius:\'5px\';\n"
        "border-top-right-radius:\'5px\';\n"
        "border-bottom-right-radius:\'5px\';\n"
        "font: 11pt \"Montserrat SemiBold\";\n"
        "width: \'95px\';\n"
        "height: \'30px\';")
        else:
                self.tap.setEnabled(True)
                self.tap.setStyleSheet("color: \"#ffffff\";\n"
        "background-color: rgb(111, 81, 237);\n"
        "border: 1px solid rgb(111, 81, 237) ;\n"
        "border-top-left-radius:\'5px\';\n"
        "border-bottom-left-radius:\'5px\';\n"
        "border-top-right-radius:\'5px\';\n"
        "border-bottom-right-radius:\'5px\';\n"
        "font: 11pt \"Montserrat SemiBold\";\n"
        "width: \'95px\';\n"
        "height: \'30px\';")

###########????????????????

########??? TOOLBAR ###########################################
        self.canv = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canv, self.centralwidget)
        self.tarTB.addWidget(self.toolbar)
        self.tfrTB.addWidget(self.toolbar)
        self.tapTB.addWidget(self.toolbar)
        self.ganttTB.addWidget(self.toolbar)
########???###########################################




########??? Buttons ##################################
        self.back.clicked.connect(self.goBack)
        self.gantt.clicked.connect(self.displayGantt)
        self.tfr.clicked.connect(self.displayTFR)
        self.tap.clicked.connect(self.displayTAP)
        self.tar.clicked.connect(self.displayTAR)
        self.checkBox.clicked.connect(self.displayGrid)
########???###########################################

        self.displayGantt()

        listToStr = ', '.join([str(elem) for elem in self.flowShopSchedule.sequence])
        self.sigma.setText(listToStr)
        self.c_max.setText(str(self.flowShopSchedule.makespan))
        self.tt.setText(str(self.flowShopSchedule.totalTardiness))


    def goBack(self, widget):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)

    def goHome(self, widget):
        widget.setCurrentIndex(0)

        for i in range(widget.count(), 0, -1):
            widget.removeWidget(widget.widget(i))


##################################!
    def displayTFR(self):
        self.plots.setCurrentWidget(self.tfrPlot)

        self.tfr.setEnabled(False)
        self.gantt.setEnabled(True)
        self.tar.setEnabled(True)

        self.gantt.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        self.tfr.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(55, 59, 84);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")



        self.tar.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        if len(self.flowShopSchedule.stopPreparationRate):
            self.tap.setEnabled(True)

            self.tap.setStyleSheet("color: \"#ffffff\";\n"
    "background-color: rgb(111, 81, 237);\n"
    "border: 1px solid rgb(111, 81, 237) ;\n"
    "border-top-left-radius:\'5px\';\n"
    "border-bottom-left-radius:\'5px\';\n"
    "border-top-right-radius:\'5px\';\n"
    "border-bottom-right-radius:\'5px\';\n"
    "font: 63 11pt \"Montserrat SemiBold\";\n"
    "width: \'95px\';\n"
    "height: \'30px\';")

        plt.clf()

        try:
            self.tfrTB.removeWidget(self.toolbar)
            self.plotTFR.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None

        except Exception as e:
            print(e)
            pass

        self.canv = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canv, self.centralwidget)
        self.tfrTB.addWidget(self.toolbar)
        self.plotTFR.addWidget(self.canv)


        machines = []
        tfr = self.flowShopSchedule.operatingRate
        for i in range(len(tfr)):
                machines.append('M' + str(i+1))


        self.canv.gnt.bar(machines,tfr, color=colors)

        for index, value in enumerate(tfr):
                self.canv.gnt.text(index, value, str(value)[:6], ha= 'center', va='bottom', color = colors[index])
        self.canv.draw()
##################################!

    def displayTAP(self):
        self.plots.setCurrentWidget(self.tapPlot)

        self.tfr.setEnabled(True)
        self.gantt.setEnabled(True)
        self.tar.setEnabled(True)

        self.gantt.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")



        self.tfr.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        self.tar.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        if len(self.flowShopSchedule.stopPreparationRate):

            self.tap.setEnabled(False)
            self.tap.setStyleSheet("color: \"#ffffff\";\n"
    "background-color: rgb(55, 59, 84);\n"
    "border: 1px solid rgb(111, 81, 237) ;\n"
    "border-top-left-radius:\'5px\';\n"
    "border-bottom-left-radius:\'5px\';\n"
    "border-top-right-radius:\'5px\';\n"
    "border-bottom-right-radius:\'5px\';\n"
    "font: 63 11pt \"Montserrat SemiBold\";\n"
    "width: \'95px\';\n"
    "height: \'30px\';")

        plt.clf()

        try:
            self.tapTB.removeWidget(self.toolbar)
            self.plotTAP.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None

        except Exception as e:
            print(e)
            pass

        self.canv = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canv, self.centralwidget)
        self.tapTB.addWidget(self.toolbar)
        self.plotTAP.addWidget(self.canv)


        machines = []
        tap = self.flowShopSchedule.stopPreparationRate
        for i in range(len(tap)):
                machines.append('M' + str(i+1))


        self.canv.gnt.bar(machines,tap, color=colors)

        for index, value in enumerate(tap):
                self.canv.gnt.text(index, value, str(value)[:6], ha= 'center', va='bottom', color = colors[index])
        self.canv.draw()


##################################!
    def displayTAR(self):
        self.plots.setCurrentWidget(self.tarPlot)

        self.tfr.setEnabled(True)
        self.gantt.setEnabled(True)
        self.tar.setEnabled(False)

        self.gantt.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        self.tar.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(55, 59, 84);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        if len(self.flowShopSchedule.stopPreparationRate):
            self.tap.setEnabled(True)
            self.tap.setStyleSheet("color: \"#ffffff\";\n"
    "background-color: rgb(111, 81, 237);\n"
    "border: 1px solid rgb(111, 81, 237) ;\n"
    "border-top-left-radius:\'5px\';\n"
    "border-bottom-left-radius:\'5px\';\n"
    "border-top-right-radius:\'5px\';\n"
    "border-bottom-right-radius:\'5px\';\n"
    "font: 63 11pt \"Montserrat SemiBold\";\n"
    "width: \'95px\';\n"
    "height: \'30px\';")

        self.tfr.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        plt.clf()

        try:
            self.tarTB.removeWidget(self.toolbar)
            self.plotTAR.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None

        except Exception as e:
            print(e)
            pass

        self.canv = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canv, self.centralwidget)
        self.tarTB.addWidget(self.toolbar)
        self.plotTAR.addWidget(self.canv)


        machines = []
        tar = self.flowShopSchedule.stopRate

        for i in range(len(tar)):
                machines.append('M' + str(i+1))

        self.canv.gnt.bar(machines,tar, color=colors)

        for index, value in enumerate(tar):
                self.canv.gnt.text(index, value, str(value)[:6], ha= 'center', va='bottom', color = colors[index])
        self.canv.draw()
##################################!

##################################!
    def displayGrid(self):
            self.gridValue = not self.gridValue
            self.displayGantt()


##################################!

##################################!
    def displayGantt(self):
        self.plots.setCurrentWidget(self.ganttPlot)

        self.tfr.setEnabled(True)
        self.gantt.setEnabled(False)
        self.tar.setEnabled(True)

        self.tfr.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        self.gantt.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(55, 59, 84);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        if len(self.flowShopSchedule.stopPreparationRate):

            self.tap.setEnabled(True)

            self.tap.setStyleSheet("color: \"#ffffff\";\n"
    "background-color: rgb(111, 81, 237);\n"
    "border: 1px solid rgb(111, 81, 237) ;\n"
    "border-top-left-radius:\'5px\';\n"
    "border-bottom-left-radius:\'5px\';\n"
    "border-top-right-radius:\'5px\';\n"
    "border-bottom-right-radius:\'5px\';\n"
    "font: 63 11pt \"Montserrat SemiBold\";\n"
    "width: \'95px\';\n"
    "height: \'30px\';")

        self.tar.setStyleSheet("color: \"#ffffff\";\n"
"background-color: rgb(111, 81, 237);\n"
"border: 1px solid rgb(111, 81, 237) ;\n"
"border-top-left-radius:\'5px\';\n"
"border-bottom-left-radius:\'5px\';\n"
"border-top-right-radius:\'5px\';\n"
"border-bottom-right-radius:\'5px\';\n"
"font: 63 11pt \"Montserrat SemiBold\";\n"
"width: \'95px\';\n"
"height: \'30px\';")

        plt.clf()


        try:
            self.tarTB.removeWidget(self.toolbar)
            self.plotTAR.removeWidget(self.canv)

            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None

        except Exception as e:
            print(e)
            pass

        self.canv = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar2QT(self.canv, self.centralwidget)
        self.ganttTB.addWidget(self.toolbar)
        self.plotGANTT.addWidget(self.canv)

        self.canv.gnt.set_ylim(0, 50)

        self.canv.gnt.set_xlim(0, self.flowShopSchedule.makespan + self.flowShopSchedule.makespan//10)

        self.canv.gnt.set_xlabel('')
        self.canv.gnt.set_ylabel('Machines')



        labels = []
        y_ticks = []
        for i in range(len(self.flowShopSchedule.timeMatrix)):
                labels.append('M' + str(i+1))
                y_ticks.append(15 + i * 10)
        labels.reverse()

        self.canv.gnt.set_yticks(y_ticks)


        self.canv.gnt.set_yticklabels(labels)


        colors = ['#FEB800', '#33D6A0', '#6F52ED', '#FE4C61', '#06A6FF', '#FF7A01', '#FF66B3', '#4DD1BA', '#FA656A', '#477CFF']

        for i in range(0, len(self.flowShopSchedule.timeMatrix)):
                data = [(self.flowShopSchedule.timeMatrixStart[i][j], self.flowShopSchedule.timeMatrix[i][j]-self.flowShopSchedule.timeMatrixStart[i][j]) for j in range(len(self.flowShopSchedule.timeMatrix[0]))]
                self.canv.gnt.broken_barh(data, (10 * len(self.flowShopSchedule.timeMatrix) - 10 * i + 2.5, 5), color=colors)

        minor_ticks = np.arange(0, self.flowShopSchedule.makespan + 5, 1)

        if self.gridValue:
                self.ax = plt.gca()
                self.ax.set_xticks(minor_ticks, minor=True)

                self.ax.grid(True, axis='x',which="major", alpha=0.2, color='#373B54')
                self.ax.grid(True, axis='x',which="minor", alpha=0.1, color='#373B54')

        self.canv.draw()

##################################!
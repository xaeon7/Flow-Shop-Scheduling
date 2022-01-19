from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

import functions.buttons.navigation as navigation

from screens.JobsScreen import JobsMatrixInput

from constants.screens import screens
class StartScreen(QMainWindow):
    def __init__(self, widget):

        super(StartScreen, self).__init__()
        loadUi("src/screens/ui/StartScreen.ui",self)
        
        #? Initialize settings
        self.algorithm.setEnabled(False)
        self.optimize.setEnabled(False)
        
        #? Link settings
        self.preparation.clicked.connect(self.updateAlgo)
        self.delay.clicked.connect(self.updateOptimize)

        #? Handle navigation
        navigation.handleStartPageNavigation(self, widget = widget, screen = screens["Start"] )

    def updateAlgo(self):
        self.algorithm.setEnabled(self.preparation.isChecked())

    def updateOptimize(self):
        self.optimize.setEnabled(self.delay.isChecked())

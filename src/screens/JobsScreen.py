from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

import styles.styles as styles

import functions.tables.createTable as createTable
import functions.tables.fillTable as fillTable
import functions.tables.importTable as importTable


import functions.buttons.navigation as navigation

from constants.screens import screens
class JobsMatrixInput(QMainWindow):
    
    def __init__(self, widget):
        super(JobsMatrixInput, self).__init__()

        #? load Ui file
        loadUi("src/screens/ui/JobsScreen.ui",self)

        #? Handle navigation
        navigation.handleNavigation(self, widget = widget, screen = screens["JobsInput"])

        #? Initialize the state of next button
        self.continueButton.setStyleSheet(styles.continueButtonDisabled)
        self.continueButton.setEnabled(False)

        #? Track button updates
        self.matrixTable.itemChanged.connect(lambda : navigation.updateNextButton(self, widget = widget, screen = screens["JobsInput"]))

        #? Create a table with n jobs and m machines
        createTable.jobTable(self, columns = widget.nb_jobs, rows = widget.nb_machines, widget = widget)

        #? Handle file import
        self.importButton.clicked.connect(lambda : importTable.jobsTable(self, 2, 2, createTable, fillTable, widget = widget))

        #? Initialize Errors
        self.errorType = 0



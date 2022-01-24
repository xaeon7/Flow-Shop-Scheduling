from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

import styles.styles as styles

import functions.tables.createTable as createTable
import functions.tables.importTable as importTable

import functions.buttons.navigation as navigation

from constants.screens import screens

import errors.errors as errors

class PrepInput(QMainWindow):
    def __init__(self, widget):
        super(PrepInput, self).__init__()
        
        #? load Ui file
        loadUi("src/screens/ui/PreparationScreen.ui",self)
        
        #? Handle navigation
        navigation.handleNavigation(self, widget = widget, screen = screens["PreparationInput"])
        
        #? Initialize the state of next button
        self.continueButton.setStyleSheet(styles.continueButtonDisabled)
        self.continueButton.setEnabled(False)
        
        #? Create a table with n jobs and m machines
        createTable.preparationTable(self, widget = widget)
        
        #? Initialize Errors
        self.errorExists = False
        
        #? Handle file import
        self.importButton.clicked.connect(lambda : importTable.preparationTables(self, 2, 2, widget = widget))

        #? Track button updates
        for machineTable in range(widget.nb_machines):
            tab = self.prepTabs.widget(machineTable).children()[1]
            tab.itemChanged.connect(lambda : navigation.updateNextButton(self, widget = widget, screen = screens["PreparationInput"])) 
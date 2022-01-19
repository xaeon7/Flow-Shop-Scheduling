import styles.styles as styles

from functions.navigation.goNext import goNext
from functions.navigation.goBack import goBack
from functions.navigation.goHome import goHome

from constants.screens import screens

def handleStartPageNavigation(self):
    self.start.clicked.connect(self.gotoJobsInput)

def handleNavigation(self, widget, screen):
    self.continueButton.clicked.connect(lambda : goNext(self, widget = widget, screen = screen))
    self.backButton.clicked.connect(lambda : goBack(self, widget = widget))
    self.logo.clicked.connect(lambda : goHome(self, widget = widget))
    
def updateNextButton(self, widget, screen):
     
    if screen == screens["JobsInput"] :
        buttonIsEnables = all([all([self.matrixTable.item(row, col) for col in range(widget.nb_jobs)]) for row in range(widget.nb_machines)])
    
    elif screen == screens["DelayInput"]:
        buttonIsEnables= all([self.matrixTable.item(0, col) for col in range(widget.nb_jobs)])
    
    elif screen == screens["PreparationInput"]:
        flag = []
        
        for mtab in range(widget.nb_machines):
            tab = self.prepTabs.widget(mtab).children()[1]
            flag.append(all([tab.item(row, col)for col in range(widget.nb_jobs) for row in range(widget.nb_jobs)]))
            
        buttonIsEnables = all(flag)
    
    if buttonIsEnables:
        self.continueButton.setStyleSheet(styles.continueButtonEnabled)
        self.continueButton.setEnabled(True)
    else:
        self.continueButton.setStyleSheet(styles.continueButtonDisabled)
        self.continueButton.setEnabled(False)
        
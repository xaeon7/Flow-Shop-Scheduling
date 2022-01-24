from constants.screens import screens

from functions.navigation.goToJobsScreen import goToJobsScreen
from functions.navigation.goToPlotsScreen import goToPlotsScreen
from functions.navigation.goToPreparationScreen import goToPreprationScreen
from functions.navigation.goToDelayScreen import goToDelayScreen

from errors.handleFileReading import handleFileReading

def goNext(self, widget, screen):
    
    if screen == screens["Start"] :
        
        goToJobsScreen(self, widget = widget)
    
        #? Assign Settings
        widget.nb_jobs=self.nb_jobs.value()
        widget.nb_machines=self.nb_machines.value()
        widget.delay=self.delay.isChecked()
        widget.prep=self.preparation.isChecked()
        widget.algo = self.algorithm.currentIndex()
        widget.optimize = self.optimize.currentIndex()
    
    else:     
        #? Read Tables
        handleFileReading(self,  widget = widget, screen = screen)      
          
        if screen == screens["JobsInput"] and not self.errorExists:
            #? Go to the next Screen
            if widget.delay:
                goToDelayScreen(widget = widget)
            
            elif widget.prep:
                goToPreprationScreen(widget = widget)
                            
            elif widget.jobsMatrix :
                goToPlotsScreen(widget = widget)
            
        elif screen == screens["DelayInput"] and not self.errorExists:
            
            #? Go to the next Screen
            if widget.prep:
                goToPreprationScreen(widget = widget)
                            
            elif widget.jobsMatrix :
                goToPlotsScreen(widget = widget)
        
        elif screen == screens["PreparationInput"] and not self.errorExists:  
                    
            #? Go to the next Screen                    
            if widget.jobsMatrix :
                goToPlotsScreen(widget = widget)
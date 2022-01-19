import functions.tables.readTable as readTable

from constants.screens import screens

def goNext(self, widget, screen):
    
    
    #? Read Tables
    if screen == screens["JobsInput"] :
        readTable.jobsTable(self, widget = widget)
        
        if widget.delay:
            self.gotoDelayInput()
        
        elif widget.prep:
            self.gotoPrepInput()
                        
        elif widget.jobsMatrix :
            self.gotoGantt()
    
    elif screen == screens["DelayInput"]:
        readTable.delaytable(self, widget = widget)
        
        if widget.prep:
            self.gotoPrepInput()
                        
        elif widget.jobsMatrix :
            self.gotoGantt()
    
    elif screen == screens["PreparationInput"]:
        readTable.delaytable(self, widget = widget)
    


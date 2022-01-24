import functions.tables.readTable as readTable
import errors.errors as errors
import errors.warnings as warnings

from constants.screens import screens

def handleFileReading(self, widget, screen):
    
    try:
        if screen == screens["JobsInput"]:
            readTable.jobsTable(self, widget = widget)
            
        elif screen == screens["DelayInput"]:
            readTable.delayTable(self, widget = widget)
            
        elif screen == screens["PreparationInput"]:
            readTable.preparationTables(self, widget = widget)
            
    except ValueError:
        errors.valueError(self) 
        
    except AttributeError:
        pass
    
    else:
        errors.resetError(self)
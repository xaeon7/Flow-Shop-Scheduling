import styles.styles as styles

def resetError(self):
    self.errorExists = False
    self.info.setText('')  

def indexError(self):
    self.errorExists = True
    self.info.setText('Missing data, make sure to fill all the necessary cells.')  
    self.info.setStyleSheet(styles.errorMessage)
    
def valueError(self):
    self.errorExists = True
    self.info.setText('Invalid data, make sure to insert only integers.')  
    self.info.setStyleSheet(styles.errorMessage)
    
def attributeError(self):
    self.errorExists = True
    self.info.setText('There are null elements.')  
    self.info.setStyleSheet(styles.errorMessage)
    

    
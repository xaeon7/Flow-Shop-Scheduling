import styles.styles as styles
from constants.plots import plots

def plotsNavigation(self, plot):
    
    self.gantt.setEnabled(True)
    self.tfr.setEnabled(True)
    self.tar.setEnabled(True)
    
    if len(self.flowShopSchedule.stopPreparationRate):
        self.tap.setEnabled(True)
        self.tap.setStyleSheet(styles.graphTypeButtonEnabled)

    self.gantt.setStyleSheet(styles.graphTypeButtonEnabled)
    self.tar.setStyleSheet(styles.graphTypeButtonEnabled)
    self.tfr.setStyleSheet(styles.graphTypeButtonEnabled)
    
    if plot == plots["TFR"]:
        self.tfr.setEnabled(False)
        self.tfr.setStyleSheet(styles.graphTypeButtonSelected)
        
    elif plot == plots["TAP"]:
        self.tap.setEnabled(False)
        self.tap.setStyleSheet(styles.graphTypeButtonSelected)
    
    elif plot == plots["TAR"]:
        self.tar.setEnabled(False)
        self.tar.setStyleSheet(styles.graphTypeButtonSelected)
    
    elif plot == plots["Gantt"]:
        self.gantt.setEnabled(False)
        self.gantt.setStyleSheet(styles.graphTypeButtonSelected)
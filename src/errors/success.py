import styles.styles as styles

def importSuccess(self):
    self.errorExists = True
    self.info.setText('File imported successfully.')  
    self.info.setStyleSheet(styles.successMessage)
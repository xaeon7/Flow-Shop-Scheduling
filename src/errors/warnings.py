import styles.styles as styles

def inputWarning(self):
    self.errorExists = False
    self.info.setText(f'The imported table contains more than needed cells.')  
    self.info.setStyleSheet(styles.warningMessage)
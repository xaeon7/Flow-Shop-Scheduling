from screens.JobsScreen import JobsMatrixInput

def goToJobsScreen(self, widget):
    
    #? Assign Settings
    widget.nb_jobs=self.nb_jobs.value()
    widget.nb_machines=self.nb_machines.value()
    widget.delay=self.delay.isChecked()
    widget.prep=self.preparation.isChecked()
    widget.algo = self.algorithm.currentIndex()
    widget.optimize = self.optimize.currentIndex()
    
    #? Go to the next Page
    inputJobs = JobsMatrixInput(widget = widget) 
    widget.addWidget(inputJobs)
    widget.setCurrentIndex(widget.currentIndex() + 1)
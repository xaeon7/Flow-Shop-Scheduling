def jobsTable(self, widget):
    
    jobsMatrix=[[int(self.matrixTable.item(row, col).text()) for col in range(widget.nb_jobs)] for row in range(widget.nb_machines)]
    widget.jobsMatrix = jobsMatrix
    
def delaytable(self, widget):
    delaySeq=[int(self.matrixTable.item(0, col).text()) for col in range(widget.nb_jobs)]
    widget.delaySeq = delaySeq
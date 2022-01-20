def jobsTable(self, widget):
    
    jobsMatrix=[[int(self.matrixTable.item(row, col).text()) for col in range(widget.nb_jobs)] for row in range(widget.nb_machines)]
    widget.jobsMatrix = jobsMatrix
    
def delayTable(self, widget):
    delaySeq=[int(self.matrixTable.item(0, col).text()) for col in range(widget.nb_jobs)]
    widget.delaySeq = delaySeq
    
def preparationTables(self, widget):
    n, m = widget.nb_jobs, widget.nb_machines
    widget.prepMatrix=[]
    
    for machineTable in range(m):
        tab = self.prepTabs.widget(machineTable).children()[1] 
        tabData = [[int(tab.item(row, col).text()) for col in range(n)] for row in range(n)]
        widget.prepMatrix.append(tabData)
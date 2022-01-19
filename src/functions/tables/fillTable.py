from PyQt5.QtWidgets import QTableWidgetItem

def jobTable(self, matrix, widget):
    for i in range(widget.nb_machines):
        for j in range(widget.nb_jobs):
            self.matrixTable.setItem(i,j, QTableWidgetItem(str(matrix[i][j])))
            
def delayTable(self, seq, widget):
    for j in range(widget.nb_jobs):
        self.matrixTable.setItem(0,j, QTableWidgetItem(str(seq[j])))
        
def preparationTables(self, widget):
    n, m = widget.nb_jobs, widget.nb_machines
    
    for machineTab in range(m):
        tab = self.prepTabs.widget(machineTab).children()[1]
        for jobLines in range(n):
            for jobColumns in range(n):
                tab.setItem(jobLines,jobColumns, QTableWidgetItem(str(widget.prepMatrix[machineTab][jobLines][jobColumns])))


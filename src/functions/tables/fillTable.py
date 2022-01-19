from PyQt5.QtWidgets import QTableWidgetItem

def jobTable(self, matrix, widget):
    for i in range(widget.nb_machines):
        for j in range(widget.nb_jobs):
            self.matrixTable.setItem(i,j, QTableWidgetItem(str(matrix[i][j])))

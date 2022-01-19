from PyQt5.QtWidgets import QHeaderView

def jobTable(self, columns, rows, widget):
    widget.nb_jobs = columns
    widget.nb_machines = rows
    
    widget.jobsMatrix = []
    
    self.matrixTable.setRowCount(rows)
    self.matrixTable.setColumnCount(columns)
    self.matrixTable.clear()
    self.matrixTable.setHorizontalHeaderLabels(["Job "+str(i+1) for i in range(columns)])
    self.matrixTable.setVerticalHeaderLabels(["Machine "+str(i+1) for i in range(rows)])
    self.matrixTable.horizontalHeader().setStretchLastSection(True)
    self.matrixTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
from PyQt5.QtWidgets import QHeaderView,QTableWidget, QWidget,QVBoxLayout

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
    

def delayTable(self, widget):
    self.matrixTable.setRowCount(1)
    self.matrixTable.setColumnCount(widget.nb_jobs)
    self.matrixTable.clear()
    self.matrixTable.setHorizontalHeaderLabels(["Job "+str(i+1) for i in range(widget.nb_jobs)])
    self.matrixTable.setVerticalHeaderLabels(["Delay"])
    self.matrixTable.horizontalHeader().setStretchLastSection(True)
    self.matrixTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
def preparationTable(self, widget):

    #? Generate a Tab for each machine and load tables
    n, m = widget.nb_jobs, widget.nb_machines
    self.prepMatrix=[[[]*n]*n]*m
    
    for j in range(m):
        table = QTableWidget()
        
        page = QWidget()
        page.layout = QVBoxLayout()
        page.layout.addWidget(table)
        page.setLayout(page.layout)
    
        self.prepTabs.addTab(page,"Machine "+str(j+1))
        
        tab = self.prepTabs.widget(j).children()[1]
        tab.setRowCount(n)
        tab.setColumnCount(n)
        tab.clear()
        
        headers=["Job "+str(i+1) for i in range(n)]
        
        tab.setHorizontalHeaderLabels(headers)
        tab.setVerticalHeaderLabels(headers)
        tab.horizontalHeader().setStretchLastSection(True)
        tab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
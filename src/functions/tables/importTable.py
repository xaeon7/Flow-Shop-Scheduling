from PyQt5.QtWidgets import QFileDialog
from openpyxl import load_workbook
import utils.excelScripts as excelScripts

def jobsTable(self, initCol, initRow, createTable, fillTable, widget):
    
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "Import Jobs Data", "","Excel Files (*.xlsx)", options = options)
    
    if not(fileName):
        return 0
    
    wb2 = load_workbook(fileName)
    sheet = wb2.worksheets[0]
    matrix = excelScripts.readMatrix(sheet, initCol, initRow)
    
    #? Create a table that fits the imported file
    createTable.jobTable(self, rows = len(matrix), columns = len(matrix[0]), widget = widget)
    
    #? Fill the table with imported Data
    try:
        fillTable.jobTable(self, matrix, widget = widget)
    except:
        self.error.setText('The data is invalid, make sure to fill all the necessary cells.')    
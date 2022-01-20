def readMatrix(sheet, scol, srow):
    col, row = scol, srow
    matrix = []
    
    while sheet.cell(row = row, column = col).value:
        rowlst = []
        
        while sheet.cell(row = row, column = col).value:
            rowlst.append(sheet.cell(row = row, column = col).value)
            col += 1
            
        matrix.append(rowlst)
        row += 1
        col = scol
    return matrix

def readSeq(sheet, scol, srow):
    col,row = scol, srow
    seq = []
    while sheet.cell(row = row, column = col).value:
        seq.append(sheet.cell(row = row, column = col).value)
        col += 1
    return seq

def readprepMatrix(sheet, scol, srow):
    col, row = scol, srow
    tensor = []
    
    while sheet.cell(row = row, column = col).value:
        matrix = []
        
        while sheet.cell(row = row, column = col).value:
            rowlst = []
            
            while sheet.cell(row = row, column = col).value:
                rowlst.append(sheet.cell(row = row, column = col).value)
                col += 1
                
            matrix.append(rowlst)
            row += 1
            col = scol
            
        tensor.append(matrix)
        row += 2
    return tensor


def saveMatrix(matrix, sheet, scol, srow):
    nb_row = len(matrix)
    nb_col = len(matrix[0])
    sheet.cell(row = srow, column = scol).value = "JobsMatrix"
    
    for i in range(1, nb_col+1):
        sheet.cell(row = srow, column = scol+i).value = "Job " + str(i)
        
    for i in range(1, nb_row+1):
        sheet.cell(row = srow+i, column = scol).value = "Machine " + str(i)
        
        for j in range(1, nb_col+1):
            sheet.cell(row = srow+i, column = scol+j).value=matrix[i-1][j-1]

class ReportGenerator:
    def __init__(self,xlsFile,sheetno,headerrow):
        self.xlsFile = xlsFile
        self.sheetno = sheetno
        self.headerrow = headerrow
    def getDataRowCount(self):
        print "sheetrowcount: " +str( self.xlsFile.getSheetRowCount(self.sheetno))
        return self.xlsFile.getSheetRowCount(self.sheetno) 
    def report1(self):
        print "report1"
    def reportCols(self,colNums):
        report = []
        for row in range(self.getDataRowCount()):
            column = []
            for col in colNums:
                column.append(self.xlsFile.getCell(self.sheetno,row,col))
            report.append(column)
        return report
    def reportConsolidate(self,colsReport,consolidateCol):
        headers = colsReport.pop(0)
        consolidatedDataDict = {}
        
        for rowIdx, row in enumerate(colsReport):
            if row[consolidateCol] in consolidatedDataDict:
                existRow = consolidatedDataDict.get(row[consolidateCol])
                for colIdx, existCell in enumerate(existRow):
                    if str(existCell) != str(row[colIdx]):
                        existCell = str(existCell) + " | " + str(str(row[colIdx]))
                        consolidatedDataDict[row[consolidateCol]][colIdx] = existCell
            else:
                consolidatedDataDict[row[consolidateCol]]= row

        outputReport = []
        outputReport.append(headers)
        for outputLine in sorted(sorted(consolidatedDataDict.keys())):
           outputReport.append(consolidatedDataDict.get(outputLine)) 
        return outputReport

    def enumFields(self):
        self.fields = []
        for col in range(self.xlsFile.getSheetRowCount(self.sheetno)):
            value = str(self.xlsFile.getCell(self.sheetno,self.headerrow,col))
            self.fields.append(value)
        return self.fields
    def getWorkbookFromReport(self,report):
        from xlwt import Workbook
        book = Workbook()
        sheet1 = book.add_sheet('Report')
        for rowIdx,row in enumerate(report):
            for colIdx,cell in enumerate(row):
                sheet1.write(rowIdx,colIdx,cell)
        return book

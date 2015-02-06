class ReportGenerator:
    def __init__(self,xlsFile):
        self.xlsFile = xlsFile
    def report1(self):
        print "report1"
    def reportCols(self, colNums):
        report = []
        for row in range(self.xlsFile.getDataRowCount()):
            column = []
            for col in colNums:
                column.append(self.xlsFile.getCell(row,col ))
                print "column appended: " + str(self.xlsFile.getCell(row,col ))
            #report.append(self.xlsFile.getCell(row,col))
            report.append(column)
        return report

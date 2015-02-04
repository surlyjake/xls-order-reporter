from xlrd import open_workbook
from xlwt import Workbook

class XLS:
    """The Excel File"""
    def __init__(self, fileName):
        self.fileName = fileName 
        self.wb = open_workbook(self.fileName)
    def getSheet(self,sheetNum):
        return self.wb.sheet_by_index(sheetNum)
    def find(self,query):
        return '0'
    def dump(self):
        output = "sheet,row,column,value"
        sheets = self.wb.sheets()
        for s in range(len(sheets)):
            for row in range(sheets[s].nrows):
                values = []
                for col in range(sheets[s].ncols):
                    values.append(str(s))
                    values.append(str(row))
                    values.append(str(col))
                    values.append(str(sheets[s].cell(row,col).value))
                    output += ','.join(values)
                    output += "||\n"
        return output

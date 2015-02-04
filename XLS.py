from xlrd import open_workbook
from xlwt import Workbook

# Hardcoded values to find the right fields
SHEETNO=0
# Header row
HEADERROW=0


class XLS:
    """The Excel File"""
    def __init__(self, fileName):
        self.fileName = fileName 
        self.wb = open_workbook(self.fileName)
        self.sheets = self.wb.sheets()
    def getSheet(self,sheetNum):
        return self.wb.sheet_by_index(sheetNum)
    def find(self,query):
        return '0'
    def dump(self):
        output = "sheet,row,column,value"
        for s in range(len(self.sheets)):
            for row in range(self.sheets[s].nrows):
                values = []
                for col in range(self.sheets[s].ncols):
                    values.append(str(s))
                    values.append(str(row))
                    values.append(str(col))
                    values.append(str(self.sheets[s].cell(row,col).value))
                    output += ','.join(values)
                    output += "||\n"
        return output
    def enumFields(self):
        self.fields = {}
        for col in range(self.sheets[SHEETNO].ncols):
            value = str(self.sheets[SHEETNO].cell(HEADERROW,col).value)
            self.fields[value] = col
        return self.fields

#!/bin/python2



from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
from xlwt import Workbook
wb = open_workbook('simple.xls')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(str(row) + ":" + str(col) + "=" + s.cell(row,col).value)
        print ','.join(values)
ss = wb.add_sheet('second sheet')
ss.write(0,0,'Aye One')
wb.save()

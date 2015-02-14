#!/bin/python2
#from mmap import mmap,ACCESS_READ

# Hardcoded values to find the right fields
SHEETNO=0
# Header row
HEADERROW=0

import sys
from XLS import *
from MainWindow import *
from ReportGenerator import *

mainWindow = MainWindow()

if len(sys.argv) < 2:
    filename = mainWindow.getFileName()
else:
    filename = sys.argv[1]
xls = XLS(filename)

reportGenerator = ReportGenerator(xls,SHEETNO,HEADERROW)

mainWindow.buildColumnListBox(reportGenerator.enumFields())

def goButtonCallback(colNos):
    #print reportGenerator.reportCols(colNos)
    #print reportGenerator.reportConsolidate(reportGenerator.reportCols(colNos), 0)
    reportGenerator.getWorkbookFromReport(
            reportGenerator.reportConsolidate(
                reportGenerator.reportCols(colNos), 0)
            ).save(
                mainWindow.getSaveAsFileName()
            )


mainWindow.show(goButtonCallback)

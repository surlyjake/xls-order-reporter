#!/bin/python2
#from mmap import mmap,ACCESS_READ

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

#xls.enumFields().keys()
mainWindow.buildColumnListBox(sorted(xls.enumFields().keys()))

reportGenerator = ReportGenerator(xls)
def goButtonCallback(colNos):
    print "Colnos: " + str(colNos)
    print reportGenerator.reportCols(colNos)

mainWindow.show(goButtonCallback)

#print xls.dump()



#!/bin/python2
#from mmap import mmap,ACCESS_READ

from XLS import *
from MainWindow import *
from ReportGenerator import *

mainWindow = MainWindow()
xls = XLS(mainWindow.getFileName())
#print xls.dump()

reportGenerator = ReportGenerator(xls)
reportGenerator.report1()


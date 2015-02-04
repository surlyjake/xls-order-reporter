#!/bin/python2
#from mmap import mmap,ACCESS_READ

from XLS import *
from MainWindow import *

xls = XLS('simple.xls')
print xls.dump()
mainWindow = MainWindow()
mainWindow.show()


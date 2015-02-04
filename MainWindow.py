from Tkinter import * 
from tkFileDialog import askopenfilename

class MainWindow:
    def __init__(self):
        self.root = Tk()
    def getFileName(self):
        filename = askopenfilename(filetypes= [ ('Excel SpreadSheet', '*.xls')] )
        return filename
#    def show(self):
#        self.root.mainloop()
        
        
        

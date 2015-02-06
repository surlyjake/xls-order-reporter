from Tkinter import * 
from tkFileDialog import askopenfilename

class MainWindow:
    def __init__(self):
        self.root = Tk()
    def getFileName(self):
        filename = askopenfilename(filetypes= [ ('Excel SpreadSheet', '*.xls')] )
        return filename
    def buildColumnListBox(self,items):
        self.listbox = Listbox(self.root,selectmode=EXTENDED)
        self.listbox.pack()
        #print "this is items: " + str(items)
        for item in items:
            self.listbox.insert(END,item)
    def show(self,goButtonCallback):
        b = Button(self.root, text="GO!", command=lambda: goButtonCallback(self.listbox.curselection()))
        b.pack()
        self.root.mainloop()
        
        
        

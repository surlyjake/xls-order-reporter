from Tkinter import * 
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
from ttk import *

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.ScrollboxLabel = Label(self.root, text="Fields to report")
        self.ScrollboxLabel.grid(row=0,column=0,columnspan=2)
        self.ScrollboxLabel = Label(self.root, text="Field to join")
        self.ScrollboxLabel.grid(row=0,column=2,columnspan=2)
    def getFileName(self):
        filename = askopenfilename(filetypes= [ ('Excel SpreadSheet', '*.xls')] )
        return filename
    def buildColumnListBox(self,items):
        self.joinItemvar = StringVar()
        self.joinItem = Combobox(self.root, textvariable=self.joinItemvar, state='readonly')
        self.joinItem['values'] = items
        self.joinItem.grid(row=1,column=0, sticky=N)
        self.listbox = Listbox(self.root,selectmode=EXTENDED, height=20)
        self.listbox.grid(row=1,column=2)
        yscroll = Scrollbar(command=self.listbox.yview, orient=VERTICAL)
        yscroll.grid(row=1, column=3, sticky=N+S)
        self.listbox.configure(yscrollcommand=yscroll.set)
        
        #print "this is items: " + str(items)
        for item in items:
            self.listbox.insert(END,item)
    def show(self,goButtonCallback):
        b = Button(self.root, text="GO!", command=lambda: goButtonCallback(self.listbox.curselection()))
        b.grid(row=2,column=0)
        import pdb; pdb.set_trace()
        self.root.mainloop()
    def getSaveAsFileName(self):
        return asksaveasfilename(defaultextension='.xls') 

from Tkinter import * 

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.w = Label(self.root, text="Hello, world!")
        self.w.pack()
    def show(self):
        self.root.mainloop()
        
        
        

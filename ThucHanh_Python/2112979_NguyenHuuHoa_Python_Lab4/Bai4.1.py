from tkinter import Frame, Tk, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
  
        self.parent = parent
        self.initUI()
   
    def initUI(self):
        self.parent.title("Simple Menu")
  
        menuBar = Menu(self.parent)
        self.parent.config(menu=menuBar)
  
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=fileMenu)
  
    def onExit(self):
        self.quit()

root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()
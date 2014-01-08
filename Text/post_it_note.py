"""
Post-It Note Program

A basic post it note program that allows users to add post-its via
commandline and then posts them on the screen.

"""

import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        #Creates all widgets
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable) #Create the widget
        self.entry.grid(column=0, row=0, sticky = 'EW') #add it to layout manager
        self.entry.bind("<Return>", self.onPressEnter)
        self.entryVariable.set(u"What do you need to remember?")
        
        button = Tkinter.Button(self,text=u"Save", command=self.onButtonClick)
        button.grid(column=1, row = 0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="blue",bg="yellow")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Nothing saved")
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
    def onButtonClick(self): #Event Handler
        self.labelVariable.set(self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

        
    def onPressEnter(self,event): #Event Handler
        self.labelVariable.set(self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
if __name__== "__main__":
    app = simpleapp_tk(None)
    app.title('Post-It Note Program')
    app.mainloop()

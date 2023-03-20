import tkinter as tk
class RetryButton(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs) # Inheritance- Intialising tKinter frame
        # *args and **kwargs are used as our functions arguments, when no.of parameters to be passed are not known.
        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel
        self.button = None
        self.createRetryButton()
    def createRetryButton(self):
        self.button = tk.Button(self, text="RETRY", command=self.reset, font=(self.parent.typingFont, 12))
        self.button.grid(row=0, column=0)
    def reset(self):
        self.parent.totalReset()
        # Function is in the main frame. It'll call reset function in all the files.
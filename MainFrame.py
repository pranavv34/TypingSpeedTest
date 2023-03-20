import tkinter as tk
from MovingText import MovingText
from UserEntry import UserEntry
from Timer import Timer
from RetryButton import RetryButton
from StatsFrame import StatsFrame
from WidgetModel import WidgetModel
import pyglet

class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # configurations for the outer frame
        self.parent = parent
        self.parent.title("The Ultimate Typing Test")
        self.bg = tk.PhotoImage(file="background.png")
        self.bgLabel = tk.Label(self, image=self.bg)
        self.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.pack(anchor=tk.CENTER)
        self.parent.config(bg='black')
        self.parent.minsize(960, 340)
        self.parent.maxsize(1920, 1080)
        # getting the data and creating an instance of WidgetModel
        self.widgetModel = WidgetModel()
        self.typingFont = "Raleway"
        pyglet.font.add_file("Raleway-Medium.ttf")
        # designing the subframes
        self.timer = Timer(self)
        self.timer.pack(anchor=tk.CENTER, pady=(10, 10))

        self.movingText = MovingText(self)
        self.movingText.pack(anchor=tk.CENTER)
        self.movingText.grid_propagate(0)

        self.entry = UserEntry(self)
        self.entry.pack(anchor=tk.CENTER, pady=(30, 0))

        self.retryButton = RetryButton(self)
        self.retryButton.pack(anchor=tk.CENTER, pady=(10, 65))

        self.statsFrame = StatsFrame(self)
        self.statsFrame.place(relx=1.0, rely=1.0, x=0, y=-159, anchor="ne")

    def totalReset(self):
        self.widgetModel.reset()
        self.movingText.reset()
        self.entry.reset()
        self.timer.reset()
if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()

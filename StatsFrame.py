import tkinter as tk
from tkinter import ttk


class StatsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel
        self.config(bg='black', relief=tk.RAISED, bd=5)
        self.createLabels()
        #self.createHighscoreLabels()
        self.update_self()
    def createLabels(self):
        self.wpmScoreLabel = tk.Label(self, text="AVERAGE SPEED: 0 WPM", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.wpmScoreLabel.grid(row=0, column=5)
        self.accuracyScoreLabel= tk.Label(self, text="ACCURACY: 0%", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.accuracyScoreLabel.grid(row=1, column=5)

        self.errorsScoreLabel = tk.Label(self, text="NUMBER OF ERRORS:0", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.errorsScoreLabel.grid(row=2, column=5)
        self.netresultScoreLabel = tk.Label(self, text="NET RESULT:0 WPM", font=(self.parent.typingFont,20), bg="black",
                                         fg='white')
        self.netresultScoreLabel.grid(row=4, column=5)

    def calculateWpm(self):
        num_of_words = ((self.widgetModel.char_count+1) / 5.0)
        wpm = round((num_of_words*60)/45,2)
        if wpm < 0:
            wpm = 0
        return wpm

    def calculateAccuracy(self):
        total_correct_char = self.widgetModel.char_count-self.widgetModel.mistyped_char_count
        total_char = self.widgetModel.char_count
        if total_char == 0 or total_correct_char==0:
            return 0.0
        return round(((total_correct_char)/ (total_char)) * 100.0, 2)

    def netresult(self):
        net=(self.calculateWpm()*self.calculateAccuracy())/100
        return round(net,2)

    def update_self(self):
        if self.widgetModel.started and self.widgetModel.ended:
            # update the words per minute stat
            new_wpm = self.calculateWpm()
            self.wpmScoreLabel.config(text="AVERAGE SPEED:{} WPM".format(str(new_wpm)))
            self.accuracyScoreLabel.config(text="ACCURACY: {}%".format(str(self.calculateAccuracy())))
            self.errorsScoreLabel.config(text="NUMBER OF ERRORS: {}".format(str(self.widgetModel.mistyped_word_count)))
            self.netresultScoreLabel.config(text="NET RESULT: {} WPM".format(str(self.netresult())))
        self.parent.parent.after(100, self.update_self)




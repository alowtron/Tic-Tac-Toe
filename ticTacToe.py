import tkinter as tk

#application
class main:
    def __init__(self):
        self.turn = 'O'
        self.createWindow()
        self.createButtons()
        self.placeButtons()

    def createWindow(self):
        self.window = tk.Tk()
        self.window.title = 'Tic Tac Toe'
    
    def createButtons(self):
        self.button1 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(1))
        self.button2 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(2))
        self.button3 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(3))
        self.button4 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(4))
        self.button5 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(5))
        self.button6 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(6))
        self.button7 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(7))
        self.button8 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(8))
        self.button9 = tk.Button(self.window, text = '-', width = 20, height = 10, command = lambda: self.buttonPress(9))
        
    def checkForWin(self):
        if ((self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O') or 
                (self.button4['text'] == 'O' and self.button5['text'] == 'O' and self.button6['text'] == 'O') or
                (self.button7['text'] == 'O' and self.button8['text'] == 'O' and self.button9['text'] == 'O') or
                (self.button1['text'] == 'O' and self.button4['text'] == 'O' and self.button7['text'] == 'O') or
                (self.button2['text'] == 'O' and self.button5['text'] == 'O' and self.button8['text'] == 'O') or
                (self.button3['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O') or
                (self.button1['text'] == 'O' and self.button5['text'] == 'O' and self.button9['text'] == 'O') or
                (self.button3['text'] == 'O' and self.button5['text'] == 'O' and self.button7['text'] == 'O')):
            self.winnerLabel = tk.Label(self.window, text = 'O Wins!')
            self.winnerLabel.grid(row = 4, column = 2)
        if ((self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X') or 
                (self.button4['text'] == 'X' and self.button5['text'] == 'X' and self.button6['text'] == 'X') or
                (self.button7['text'] == 'X' and self.button8['text'] == 'X' and self.button9['text'] == 'X') or
                (self.button1['text'] == 'X' and self.button4['text'] == 'X' and self.button7['text'] == 'X') or
                (self.button2['text'] == 'X' and self.button5['text'] == 'X' and self.button8['text'] == 'X') or
                (self.button3['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X') or
                (self.button1['text'] == 'X' and self.button5['text'] == 'X' and self.button9['text'] == 'X') or
                (self.button3['text'] == 'X' and self.button5['text'] == 'X' and self.button7['text'] == 'X')):
            self.winnerLabel = tk.Label(self.window, text = 'X Wins!')
            self.winnerLabel.grid(row = 4, column = 2)
        return
    
    def placeButtons(self):
        self.button1.grid(row = 1, column = 1)
        self.button2.grid(row = 1, column = 2)
        self.button3.grid(row = 1, column = 3)
        self.button4.grid(row = 2, column = 1)
        self.button5.grid(row = 2, column = 2)
        self.button6.grid(row = 2, column = 3)
        self.button7.grid(row = 3, column = 1)
        self.button8.grid(row = 3, column = 2)
        self.button9.grid(row = 3, column = 3)

    def buttonPress(self, buttonNumber):
        if buttonNumber == 1:
            if self.button1['text'] != '-':
                return
            elif self.turn == 'O':
                self.button1['text'] = 'O'
                self.turn = 'X'
            else:
                self.button1['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 2:
            if self.button2['text'] != '-':
                return
            elif self.turn == 'O':
                self.button2['text'] = 'O'
                self.turn = 'X'
            else:
                self.button2['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 3:
            if self.button3['text'] != '-':
                return
            elif self.turn == 'O':
                self.button3['text'] = 'O'
                self.turn = 'X'
            else:
                self.button3['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 4:
            if self.button4['text'] != '-':
                return
            elif self.turn == 'O':
                self.button4['text'] = 'O'
                self.turn = 'X'
            else:
                self.button4['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 5:
            if self.button5['text'] != '-':
                return
            elif self.turn == 'O':
                self.button5['text'] = 'O'
                self.turn = 'X'
            else:
                self.button5['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 6:
            if self.button6['text'] != '-':
                return
            elif self.turn == 'O':
                self.button6['text'] = 'O'
                self.turn = 'X'
            else:
                self.button6['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 7:
            if self.button7['text'] != '-':
                return
            elif self.turn == 'O':
                self.button7['text'] = 'O'
                self.turn = 'X'
            else:
                self.button7['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 8:
            if self.button8['text'] != '-':
                return
            elif self.turn == 'O':
                self.button8['text'] = 'O'
                self.turn = 'X'
            else:
                self.button8['text'] = 'X'
                self.turn = 'O'
        if buttonNumber == 9:
            if self.button9['text'] != '-':
                return
            elif self.turn == 'O':
                self.button9['text'] = 'O'
                self.turn = 'X'
            else:
                self.button9['text'] = 'X'
                self.turn = 'O'
        self.checkForWin()



    def windowRun(self):
        self.window.mainloop()

mainWindow = main()
mainWindow.windowRun()
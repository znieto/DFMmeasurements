'''
July 2017
@author: Zoraya Nieto
'''
#======================
# imports
#======================
import tkinter as tk
def print_a():
    print("a")

class MainWindow2():
    def mainWindow():
        # Create instance
        win = tk.Tk()   
        # Add a title       
        win.title("DFM Measurements Software")

        # Adding a Label
        tk.Label(win, text="A Label").grid(column=0, row=0) 

        # Disable resizing the GUI by passing in False/False
        win.resizable(False, False)  
        #======================
        # Start GUI
        #======================
        win.mainloop()
        return None



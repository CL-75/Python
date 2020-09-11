
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import file_transfer_func
import file_transfer_gui



# Frame is a built-in frame class within Tkinter that our class will inherit
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


   # Determining window size
        self.master = master
        self.master.minsize(500, 180)
        self.master.maxsize(500, 180)

   # Window title and close program function
        self.master.title("Transfer Files")
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_transfer_func.Quit(self))
        file_transfer_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

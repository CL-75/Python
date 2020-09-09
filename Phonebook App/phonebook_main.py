#
#  Python Version: 3.8.5
#
#  Author: Casey Levy
#
#
#  File Name: phonebook_main.py
#
#
#  Purpose: Demo. Creating a phonebook application to use
#           and get practice with Tkinter and Parent/Child class relationships
#
#



from tkinter import *
import tkinter as tk

# importing our other modules/files
import phonebook_gui
import phonebook_func


# 'Frame' is the Tkinter frame class that our own class will inherit from, it is built-into Tkinter
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # defining our master frame configuration that we invoked above
        self.master = master
        self.master.minsize(500, 300)     # locking the (height, width) so it cannot be resized
        self.master.maxsize(500, 300)
        
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("Tkinter Phonebook Demo")
        self.master.configure(bg = "#F0F0F0")

        # this protocol method is a tkinter built-in method used to catch if the user clicks the upper right corner "X"
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module to keep code organized
        phonebook_gui.load_gui(self)
    



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

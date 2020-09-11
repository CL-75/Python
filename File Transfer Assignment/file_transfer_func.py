
import tkinter as tk
import shutil, os, time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import file_transfer_main
import file_transfer_gui


# Function to confirm user wants to close the app 
def Quit(self):
    if messagebox.askokcancel("Exit program?"):
        self.master.destroy()
        os._exit(0)


# Browsing the files and getting file path
def Browse(self, btn):
    if btn == "source":
        entry = self.source_disp
    if btn == "dest":
        entry = self.dest_disp

    entry.config(state='normal')
    entry.delete(0, "end")

    path = filedialog.askdirectory()
    if path:
        entry.insert(0, path + "/")
    entry.config(state = 'readonly')


# Function for checking files and displaying message based on condition
def Check(self):
    try:
        source = self.source_disp.get()
        dest = self.dest_disp.get()

        lsdir = os.listdir(source)
        files = []
        timePeriod = time.time()-86400

        for i in lsdir:
            mtime = os.path.getmtime(source + i)
            if mtime >= timePeriod:
                files.append(i)

        if files:
            for i in files:
                shutil.move(source+i, dest)
            messagebox.showinfo("Files Transfered", "Your file(s) have been successfully transferred.")
        else:
            messagebox.showinfo("No Vaild Files", "No files to transfer.")
    except:
        messagebox.showinfo("Enter Valid Directories", "Please select your Source and Destination directories.")



if __name__ == "__main__":
    pass

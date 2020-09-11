
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import file_transfer_func
import file_transfer_main


# Various buttons
def load_gui(self):

# Source folder button
    self.btn_brws1 = tk.Button(self.master,width=15,height=1,text="Source",command=lambda: file_transfer_func.Browse(self,"source"))
    self.btn_brws1.grid(row=0,column=0,padx=(20,30),pady=(40,0),sticky=W)

# Destination folder button
    self.btn_brws2 = tk.Button(self.master,width=15,height=1,text="Destination",command=lambda: file_transfer_func.Browse(self,"dest"))
    self.btn_brws2.grid(row=1,column=0,padx=(20,30),pady=(10,0),sticky=W)

# Buttong to check for files  
    self.btn_chk = tk.Button(self.master,width=15,height=2,text="Check for files...",command=lambda: file_transfer_func.Check(self))
    self.btn_chk.grid(row=2,column=0,padx=(20,30),pady=(10,10),sticky=W)

# Close program button
    self.btn_cl = tk.Button(self.master,width=15,height=2,text="Close Program",command=lambda: file_transfer_func.Quit(self))
    self.btn_cl.grid(row=2,column=2,padx=(0,20),pady=(10,10),sticky=E)


# Source/Destination path displays
    self.source_disp = tk.Entry(self.master,width=48,text='')
    self.source_disp.config(state='readonly')
    self.source_disp.grid(row=0,column=1,rowspan=1,columnspan=2,padx=(0,20),pady=(40,0),sticky=N+E+W)
    
    self.dest_disp = tk.Entry(self.master,width=48,text='')
    self.dest_disp.config(state='readonly')
    self.dest_disp.grid(row=1,column=1,rowspan=1,columnspan=2,padx=(0,20),pady=(10,0),sticky=N+E+W)



if __name__ == "__main__":
    pass

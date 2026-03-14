"""Presscotts Mortar Calculator 
Made by Discord user: corruptedgingerale////steam user: Presscott
made with the help of this guide: https://steamcommunity.com/sharedfiles/filedetails/?id=1516328874

#Intent/design
 need to determine visual layout
 then need to determine bttons in layout
 will aim to create entry field on the left hand side and output on right hand side
 
 issues 1
 how will the program change based on directed input such as grid mission vs polar/radial
 
 polar/radial requires significantly less input should the entry feilds for excess information even be discplayed?
 should the menu up date with the option
 
 my preference would be to create over arching display window for calculated information but have the entry feilds seperated by a tab display similar to older windos programs and/or TES 5 graphics settings  (fuck new age gui blocky blob asss shit)


********************************************************************************************
############################################## 
    calc display field
    
    subtext displaying current position?
##############################################

#######################
tabs  grid/polar
#######################


label:
#######################
    entry field 1
#######################

label:
#######################
    entry field 2
#######################


##############################################
big  ol' calculate button and exit button 
##############################################

********************************************************************************************

"""


# this is here is an example of tkinter that i will be using to learn from 
import tkinter as tk
from tkinter import messagebox

def show_text():
    text = entry.get()
    messagebox.showinfo("You typed", text)

# Create the root window
root = tk.Tk()
root.title("Presscotts Mortar Calculator")
root.geometry("320x520")  # width x height

# Widgets
label = tk.Label(root, text="Type something:")
label.pack(pady=(12, 4))

entry = tk.Entry(root, width=40)
entry.pack(pady=4)
entry.focus()

button_frame = tk.Frame(root)
button_frame.pack(pady=8)

show_btn = tk.Button(button_frame, text="Show", command=show_text)
show_btn.pack(side="left", padx=6)

exit_btn = tk.Button(button_frame, text="Exit", command=root.destroy)
exit_btn.pack(side="left", padx=6)

# Start the event loop
root.mainloop()



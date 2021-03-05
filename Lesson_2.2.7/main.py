# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command():
    subprocess.call("./Lesson_2.2.7/command.sh")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# number 5
# set up button to run the do_command function
# Makes the command button pass it's name to a function using lambda (7)
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping -t"))
ping_btn.pack()



# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# number 6
# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
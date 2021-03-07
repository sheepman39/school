# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    # all of this code is from step 9
    global command_textbox, url_entry

    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        url_val = "localhost"
        #url_val = "::1"
    
    if("ping" in command):
        p = subprocess.Popen([command, "-c 5", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen([command, url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

# provided save function from step 11
# Save function.
def mSave():

  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
      return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# number 5
# set up button to run the do_command function
# Makes the command button pass it's name to a function using lambda (7)
# older code, using the provided template PLTW provides for all buttons
#ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command(("ping -t")))
#ping_btn.pack()

# Modifies the ping button parameters.
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
    command=lambda:do_command("ping"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    bg="black", activebackground="gray")# Modifies the ping button parameters.
ping_btn.pack() 

# step 8/12
# Modifies the ping button parameters.
nslookup_btn = tk.Button(frame, text="Click to see the IP of a website", 
    command=lambda:do_command("nslookup"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    bg="black", activebackground="gray")
nslookup_btn.pack() 

tracer_btn = tk.Button(frame, text='Click to see the route to a website',
    command=lambda:do_command("traceroute"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    bg="black", activebackground="gray") 
tracer_btn.pack()

# save button step 11
save_btn = tk.Button(frame, text='Click to save the results',
    command=lambda:mSave(),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    bg="black", activebackground="gray") 
save_btn.pack()

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
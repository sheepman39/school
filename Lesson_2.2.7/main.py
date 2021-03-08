# p227_starter_one_button_shell.py
import os
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    
    # all of this code is from step 9
    global command_textbox, url_entry

    # removes any previous text 
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        url_val = "localhost"
        #url_val = "::1"
    
    # Since replit does not work with these commands, I added a try/except block to catch and report those errors
    try:

      # since the ping command requires a special argument, this helps control that
      if(os.uname().sysname == "Linux"):
        if("ping" in command):
          
          # What the book tells you to do IS WRONG
          # the formatting for the command is supposed to look like this
          p = subprocess.Popen([command, "-c 5", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        else:
        
          # as said previously, if you have a command that does not require arguments, this is the proper formatting to run a command
          p = subprocess.Popen([command, url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

        # returns the results of the command to the text box
        cmd_results, cmd_errors = p.communicate()
        command_textbox.insert(tk.END, cmd_results)
        command_textbox.insert(tk.END, cmd_errors)
      else:
        command_textbox.insert(tk.END,"This is an unsupported system. Currently, this program only supports Linux systems.")
    except:
      
      # if an error happens, put it here
      command_textbox.insert(tk.END, "ERROR: Command not found.  Your system may be incompatable. This should be expected if you are using Replit.  Windows/MacOS version coming soon")

# provided save function from step 11
# Save function.
def mSave():

  # this was all provided by the book
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
      return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

# root frame is placed
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
    fg='white',
    relief="flat",
    cursor="heart",
    bg="black", activebackground="gray")# Modifies the ping button parameters.
ping_btn.pack() 

# step 8/12
# Modifies the nslookup button parameters.
nslookup_btn = tk.Button(frame, text="Click to see the IP of a website", 
    command=lambda:do_command("nslookup"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    fg='white',
    relief="flat",
    cursor="heart",
    bg="black", activebackground="gray")
nslookup_btn.pack() 

# tracer button
tracer_btn = tk.Button(frame, text='Click to see the route to a website',
    command=lambda:do_command("traceroute"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    fg='white',
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
    fg='white',
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
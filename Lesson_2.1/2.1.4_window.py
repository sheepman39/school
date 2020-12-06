##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# here is a site with some easy-to-use documentation
# https://www.tutorialspoint.com/python/tk_toplevel.htm
# for number 7, look at line 13

# main window
root = tk.Tk()
root.title("Authorization")
root.wm_geometry("200x200")

# create empty frame
frame_login = tk.Frame(root)
root.mainloop()

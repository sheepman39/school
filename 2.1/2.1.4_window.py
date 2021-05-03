##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk
import tkinter.scrolledtext as tksc

password = None
# step 21+22
def test_my_button():
  global password
  
  frame_auth.tkraise()

  # step 26 
  password = ent_password.get()
  user_password = tk.Label(frame_auth, text=password)
  user_password.pack()

# here is a site with some easy-to-use documentation
# https://www.tutorialspoint.com/python/tk_toplevel.htm
# for number 7, look at line 13

# main window
root = tk.Tk()

# step 7
root.title("Authorization")

root.wm_geometry("200x300")

# step 8 copy and paste
# create empty frame
frame_login = tk.Frame(root)

# new authorization frame
frame_auth = tk.Frame(root)

# step 9 + 19
frame_login.grid(row = 0, column = 0, sticky="news")

# step 20
frame_auth.grid(row = 0, column = 0, sticky = "news")

# step 10
lbl_username = tk.Label(frame_login, text='Username:',font="Courier",foreground="black")
lbl_username.pack(padx=50)

# 16 provided code
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

# steps 11-14ish
# use foreground="<color>" to change text color
lbl_password = tk.Label(frame_login,text="Password:",font="Courier",foreground="black")
lbl_password.pack(pady=25)

# step 17
ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)

# 2.1.6 stuff
bt_image = tk.PhotoImage(file="Lesson_2.2.6/button.gif")
bt_image = bt_image.subsample(10,10)

# step 18 + 23
btn_login = tk.Button(frame_login, text="Hack?", command =test_my_button, image=bt_image)
btn_login.pack(pady=25)

# step 21
frame_login.tkraise()

test_textbox = tksc.ScrolledText(frame_auth)
# this line is broken somehow even tho it is the same stuff from the book.  not sure why
test_textbox.configure(frame_auth, height=10, width=50)

root.mainloop()

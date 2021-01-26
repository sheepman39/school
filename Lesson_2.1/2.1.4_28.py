import tkinter as tk

# number 28

root = tk.Tk()
root.wm_geometry("150x175")

blue = tk.Label(root,background="blue",width=10,height=5).grid(column=0,row=0)
green = tk.Label(root,background="green",width=5,height=5).grid(column=1,row=0)
red = tk.Label(root,background="red",width=10,height=5).grid(column=0,row=1)
yellow = tk.Label(root,background="yellow",width=5,height=5).grid(column=1,row=1)


root.mainloop()

# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircteownlo app
my_auth = mfg.MultiFactorAuth()
my_auth.set_authorization('admin',"th!s!sAStrongP@$$Word" )
# set the users authentication information
question = "What is the krabby patty secret formula?"
answer = "yes, but only on tuesdays"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()

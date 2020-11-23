# Module multifactorgui.py
import tkinter as tk
import tkinter.messagebox as mb

# MultiFactorAuth is a class with three frames: 
#    an authorization (username/password) frame
#    an authentication (information factor) frame
#    the restircted applicaiton frame
# Users must pass all authorization and authentication steps to access the restricted app

class MultiFactorAuth(tk.Tk):

  # authorization and authentication info
  username = ""
  password = ""
  security_question = ""
  answer = ""

  # save username and password
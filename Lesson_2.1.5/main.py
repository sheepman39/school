##############################################################################
# a215_security_checklist.py
##############################################################################

print("Let's check your security. Answer y or n to each of the questions.")

phish = input("Can you recognize phishing emails? ")
pw = input("Is your password strong? ")
auth = input("Do you use multi-factor authentication? ")
enc = input("Do you know how to encrypt sensitive information? ")

# problem 3
# pretty much these ALL need to be yes in order to have good credit
if (phish =='y' and pw =='y' and auth == 'y' and enc == "y"):

  print("You got good credit.")

else:

  print("You got bad credit.")


# problem 5
if (phish =='y' or pw =='y' or auth == 'y' or enc == "n"):
  print("you got bad credit")
else:
  print("you got good credit.")
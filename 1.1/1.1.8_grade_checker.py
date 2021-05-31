#   a118_grades.py
# this is known as a tuple and is like a list, but the values cannot be changed
my_courses = ("English","CS","Band")

# while this is true, it will infinetly loop around
check_grades = True
while (check_grades):
  
  # this will ask you for your current grade in each of the courses in my_course
  for course in my_courses:

    print("Enter your points for " + course)
    a = int(input("Points -> "))
    
    # checks what the grade is
    if (a >= 90):
      print("A")
    elif (a >= 80):
      print("B")
    elif (a >= 70):
      print("C")
    elif (a >= 60):
      print("D")
    else:
      print("F")
    
    redo = input("Do you need to re-do these grades? (y/n)")
    
    if (redo == "y"):
      check_grades = True
    else:
      check_grades = False

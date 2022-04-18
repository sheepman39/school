import pyautogui
import time

# ensure that the failsafe is enabled
# DO NOT SET TO False
pyautogui.FAILSAFE = True

# list to store the coordinates
mouse_points = []

# list of passes the loop has gone through
passes = 0

# asks the user to put mouse in 4 different coordinates and stores them in mouse_points
def setup():
    
    pyautogui.alert("Setup in progress.  You will have 3 seconds in between each notification to set the location of your mouse. There will be 4 points to set",)
    
    # for loop goes through the 4 different coordinates and prompts
    for i in range(0,4):
        
        # 3 second delay to give user time to move mouse
        time.sleep(3)
        
        # gets the current position of the mouse
        currentMouseX, currentMouseY = pyautogui.position()
       
        # setup messages
        setup_messages = [
            f"First point marked as {currentMouseX}, {currentMouseY}.  Close this window and move to the second point",
            f"Second point marked as {currentMouseX}, {currentMouseY}.  Close this window and move to the third point",
            f"Third point marked as {currentMouseX}, {currentMouseY}.  Close this window and move to the fourth point",
            f"Last point marked as {currentMouseX}, {currentMouseY}.  Close this window and the program will keep your mouse moving"
        ]
        
        # adds the coordinates to the mouse_points list and sends the user the next message
        mouse_points.append((currentMouseX, currentMouseY))
        pyautogui.alert(setup_messages[i])


setup()

# while loop keeps program running indefinetly
# use ctrl+c or slam mouse into a corner while it is moving to trigger failsafe
while True:

    print("Moving the mouse....")
    
    # actually moves the mouse to the correct points
    pyautogui.moveTo(mouse_points[passes % 4][0], mouse_points[passes % 4][1], 3, pyautogui.easeInBounce)
    
    # click to ensure activity is recorded
    pyautogui.click()
    
    # adds another pass and sets a delay to 20 seconds
    passes += 1
    time.sleep(20)

import pyautogui
import time


pyautogui.FAILSAFE = True

mouse_points = []
passes = 0


def setup():

    
    pyautogui.alert("Setup in progress.  You will have 3 seconds in between each notification to set the location of your mouse. There will be 4 points to set",)
    for i in range(0,4):
        time.sleep(3)
        currentMouseX, currentMouseY = pyautogui.position()
        setup_messages = [
            f"First point marked as {currentMouseX}, {currentMouseY}.  Close this window and move to the second point",
            f"Second point marked as {currentMouseX}, {currentMouseY}.  Close this window and move to the third point",
            f"Third point marked as {currentMouseX}, {currentMouseY}.  Close this window and move to the fourth point",
            f"Last point marked as {currentMouseX}, {currentMouseY}.  Close this window and the program will keep your mouse moving"
        ]

        mouse_points.append((currentMouseX, currentMouseY))
        pyautogui.alert(setup_messages[i])


setup()
print(mouse_points)

while True:

    print("Moving the mouse....")
    pyautogui.moveTo(mouse_points[passes % 4][0], mouse_points[passes % 4][1], 3, pyautogui.easeInBounce)
    pyautogui.click()
    passes += 1
    time.sleep(20)

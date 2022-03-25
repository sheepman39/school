import requests
from PIL import Image

# file to save image to
FILE = "dog.jpg"

# opens up a file to store the cat image in
# 'wb' stands for write in binary, telling the computer to save the image as a binary
image = open(FILE,"wb")

# the API we will be using is Cat As A Service
URL = "https://place.dog/1920/1080"
URL = "https://cataas.com/"

# gets a gif from the API
response = requests.get(URL+"/c")

# if the response is good, save the image
if response.status_code == 200:
    image.write(response.content)
    im = Image.open(FILE)
    im.show()

# if not, print out an error
else:
    print("ERROR: " + response.status_code)

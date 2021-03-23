# LunarLander - main.py
# This program is just for reference,
# you cannot run it in Trinket

import gdx

my_gdx = gdx.gdx()

# First establish a connection via USB
my_gdx.open_usb()

# Then you access the sensor information.
sensor_info = my_gdx.sensor_info()

for info in sensor_info:
  sensor_number = info[0]
  sensor_description = info[1]
  sensor_units = info[2]
  print("sensor number = ", sensor_number)
  print("sensor description = ", sensor_description)
  print("sensor units = ", sensor_units)
  
# Close the connection with the sensor
my_gdx.close()

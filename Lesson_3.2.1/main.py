# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
temp_data = pd.read_csv("./Lesson_3.2.1/temperature_data.csv", header=0)   # identify the header row

# TODO #2: Use matplotlib to make a line graph
plt.plot(temp_data['Year'], temp_data['Anomaly'], color='gray')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures (1)')

# TODO #3: Plot LOWESS in a line graph
plt.plot(temp_data['Year'], temp_data['LOWESS'], color='blue')

# TODO #4: Use matplotlib to make a bar chart
plt.bar(temp_data['Year'], temp_data['Anomaly'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years

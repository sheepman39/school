# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
temp_data = pd.read_csv("./3.2.1/temperature_data.csv", header=0)   # identify the header row

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
min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

# find the min, max and calculate the sum
for i in range(0, len(temp_data['Anomaly'])):
  if (temp_data['Anomaly'][i] < min_anomaly):
    min_anomaly = temp_data['Anomaly'][i]
    min_year = temp_data['Year'][i]
  
  # extra for loop for step 25
  if (temp_data['Anomaly'][i] > max_anomaly):
    max_anomaly = temp_data['Anomaly'][i]
    max_year = temp_data['Year'][i]
  
  # step 26
  # new code inside the same for loop
  sum_anomaly = sum_anomaly + temp_data['Anomaly'][i]

  # step 27
  # calculate average
  avg_anomaly = sum_anomaly/len(temp_data['Anomaly'])

# step 28
# note this is outside of the for loop
# print the statistical values
print("The maximum anomaly is:", max_anomaly, "which occured in", max_year)
print("The minimum anomaly is:", min_anomaly, "which occured in", min_year)
print("The average anomaly is:", avg_anomaly)

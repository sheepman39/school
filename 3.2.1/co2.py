# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd
import math

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
co2_data = pd.read_csv("./3.2.1/co2_data.csv", header=0)   # identify the header row

#part of step 40
print(co2_data)

# Step 39
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)

#part of step 40
print(co2_data)

co2_data.dropna(subset=['Average'], inplace=True)

#part of step 40
print(co2_data)

# TODO #2: Use matplotlib to make a line graph
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')


# TODO #5: Calculate min, max, and avg Average and the corresponding min/max years
min_Average = co2_data['Average'][0]
max_Average = co2_data['Average'][0]
min_year = co2_data['decimal_year'][0]
max_year = co2_data['decimal_year'][0]
sum_Average = 0
avg_anomaly = 0
plt.show()

'''
# find the min, max and calculate the sum
for i in range(0, len(co2_data['Anomaly'])):
  if (co2_data['Anomaly'][i] < min_anomaly):
    min_anomaly = co2_data['Anomaly'][i]
    min_year = co2_data['decimal_year'][i]
  
  # extra for loop for step 25
  if (co2_data['Anomaly'][i] > max_anomaly):
    max_anomaly = co2_data['Anomaly'][i]
    max_year = co2_data['decimal_year'][i]
  
  # step 26
  # new code inside the same for loop
  sum_Average = sum_Average + co2_data['Average'][i]

  # step 27
  # calculate Average
  avg_Average = sum_Average/len(co2_data['Average'])

# step 28
# note this is outside of the for loop
# print the statistical values
print("The maximum Average is:", max_Average, "which occured in", max_year)
print("The minimum Average is:", min_Average, "which occured in", min_year)
print("The Average Average is:", avg_Average)
'''

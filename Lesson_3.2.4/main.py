import matplotlib.pyplot as plt
import pandas as pd

# reads the csv file
df = pd.read_csv("./Lesson_3.2.4/honey_1997.csv", header=0)

# Replaces any commas in the amount of honey produced with spaces to make converting easier
df['Value'] = df['Value'].str.replace(',', '')

# If a value is NaN, replace it with NaN
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Takes a list of all of the unique states and puts them in a list
unique_states = df['State'].unique()

# For each state, the honey_data contains the total honey from each individual year
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']

# values of production by state and by year
honey_sums = honey_data.sum()

# this stores the years that go with honey_sums
years = honey_sums.keys()

# this stores the honey values and states
all_honey = []
all_states = []

# this goes through each state, groups the data by year and adds it to the all_honey array
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(state)

# this iterates over all_honey and plots each individual state
for i in range(len(all_honey)):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)

# this sets the lables, titles, legend, and finally, displays the graph produced
plt.ylabel('Honey Production')
plt.xlabel('Year')
plt.title('Honey Production')
plt.legend()
plt.show()



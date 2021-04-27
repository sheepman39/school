import matplotlib.pyplot as plt
import pandas as pd

# reads the csv file
df = pd.read_csv("./Lesson_3.2.4/honeyOps.csv", header=0)

# Replaces any commas in the amount of honey produced with spaces to make converting easier
#df['Value'] = df['Value'].str.replace(',', '')

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

# Average graph
all_honey = []
all_states = []

# Note all_honey.append(honey_data.*mean*())
# that allows it to take the average produced from the year
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  all_honey.append(honey_data.mean())
  all_states.append(state)

# graphs the large graph
for i in range(len(all_honey)):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)

# labels
plt.ylabel('Honey Production (Meme)')
plt.xlabel('Year')
plt.title('Honey Production (Meme)')
plt.show()


all_totals = []
all_years = []

unique_years = df["Year"].unique()
# For each state, the honey_data contains the total honey from each individual year
for year in unique_years:
  totals = df[df['Year'] == year].groupby('Year')['Value']

# values of production by state and by year
totals_sums = totals.sum()

# this stores the years that go with honey_sums
years = totals_sums.keys()

# this goes through each state, groups the data by year and adds it to the all_honey array
for year in unique_years:
  total_data = df[df['Year'] == year].groupby('Year')['Value']
  all_totals.append(total_data.sum())
  all_years.append(year)

# this section is all for the main graph
# this iterates over all_honey and plots each individual state
for i in range(len(all_totals)):
  totals = all_totals[i]
  years = all_years[i]
  years_key = totals.keys()
  plt.bar(years_key, totals, label=years)

# labels
plt.ylabel('Honey Production (Means)')
plt.xlabel('Year')
plt.title('Honey Production (Means)')
plt.show()

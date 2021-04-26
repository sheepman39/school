import matplotlib.pyplot as plt
import pandas as pd

# these functions here are an insertion sort algorithm to sort dicts within a list
def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertionsort(array):
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1]['sum'] > array[j]['sum']:
            swap(array, j-1, j)
            j -= 1

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

# this will be a sorted list that will allow us to group by total size
total_states = []

# This is just for the total_states variable
for state in unique_states:
  honey_data = df[df['State'] == state]['Value']
  total_states.append({'state': state, 'sum': honey_data.sum()})

# this if statement sorts the total_states list
if __name__ == "__main__":
  insertionsort(total_states)

# this goes through each state, groups the data by year and adds it to the all_honey array
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(state)

# this section is all for the main graph
# this iterates over all_honey and plots each individual state
for i in range(len(all_honey)):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)

plt.ylabel('Honey Production')
plt.xlabel('Year')
plt.title('Honey Production')
plt.legend()
plt.show()

# Small list
# It is necessary to reset the all_honey and states lists so the new sorted data will work
all_honey = []
all_states = []

# takes the first 17 items in the total_states list 
for i in range(17):

  # finds the state that matches the sorted list so the values are in order
  honey_data = df[df['State'] == total_states[i]['state']].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(total_states[i]['state'])

# this graphs the small graph
for i in range(len(all_honey)):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)

# labels
plt.ylabel('Honey Production (Small)')
plt.xlabel('Year')
plt.title('Honey Production (Small)')
plt.legend()
plt.show()

# Medium list
all_honey = []
all_states = []

# just like the for loop above, but shifts the range to the medium group
for i in range(18, 34):
  honey_data = df[df['State'] == total_states[i]['state']].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(total_states[i]['state'])

# graphs the medium graph
for i in range(len(all_honey)):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)

# labels
plt.ylabel('Honey Production (Medium)')
plt.xlabel('Year')
plt.title('Honey Production (Medium)')
plt.legend()
plt.show()

# Large graph
all_honey = []
all_states = []

# shifts the range of the array to 35, 50
for i in range(35,50):
  honey_data = df[df['State'] == total_states[i]['state']].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(total_states[i]['state'])

# graphs the large graph
for i in range(len(all_honey)):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)

# labels
plt.ylabel('Honey Production (Large)')
plt.xlabel('Year')
plt.title('Honey Production (Large)')
plt.legend()
plt.show()

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


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./Lesson_3.2.4/honey_1997.csv", header=0)

df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

unique_states = df['State'].unique()

for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']

honey_sums = honey_data.sum()
years = honey_sums.keys()

all_honey = []
all_states = []

''' # without grouping
for state in unique_states:
  honey_data = df[df['State'] == state]['Value']
  print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)
'''  
# with grouping
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)
  
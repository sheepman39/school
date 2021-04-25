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

# with grouping
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(state)

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

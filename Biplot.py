import pandas as pd
import matplotlib.pyplot as plt

# Create the dataframe
df1 = pd.DataFrame({
  'a': [397, 682, 506, 0.6],
  'b': [608, 435, 542, 1.4],
  'c': [619, 421, 545, 1.5],
  'd': [512, 522, 551, 0.98]
}, index=["A", "B", "C", "D"])

# Reset the row names
df2 = df1.reset_index()

# Reshape the dataframe
df2 = df2.melt(id_vars='index', var_name='name', value_name='value')

# Apply the transformations
df2['value'] = df2.apply(lambda x: x['value'] * 300 if x['index'] == 'D' else x['value'] - (x['value'] * 2), axis=1)

# Plot the data
plt.figure(figsize=(8, 12))
ax = plt.gca()
df2[df2['index'] == 'D'].plot(kind='bar', x='name', y='value', color='y', ax=ax, position=0.5, width=0.2)  # Adjust the width to 0.3
df2[df2['index'] != 'D'].pivot(index='name', columns='index', values='value').plot(kind='bar', ax=ax, width=0.3)

# Set the y-axis scale
#plt.yscale('symlog', linthresh=0.01)

# Manually set y-axis ticks and labels
plt.yticks([100 * x for x in [6, 4.5, 3, 0, -2, -4, -6, -8]], [2, 1.5, 1, 0, 100, 400, 600, 800])

# Add horizontal and vertical lines
plt.axhline(y=300, color='r', linestyle='--')
#plt.axvline(x=1, color='r')


# Adjust the length of the "D" bar
for i, value in enumerate(df2['value']):
    if df2.loc[i, 'index'] == 'D':
        plt.bar(i, value, color='y', width=0.1, alpha=0.5)
plt.show()

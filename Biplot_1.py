import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Example data
df = pd.read_csv("cold_hot_neutral/counts.tab", sep='\t', index_col=0) 

# Calculate the ratio of Cold to Hot
df['cold_hot_ratio'] = df['cold'] / df['hot']

# Sort DataFrame based on cold_hot_ratio
df.sort_values(by='cold_hot_ratio', inplace=True)

# Reset the row names
df1 = df.T.reset_index()

# Reshape the dataframe
df2 = df1.melt(id_vars='index', var_name='name', value_name='value')

# Apply the transformations
df2['value'] = df2.apply(lambda x: x['value'] * 300 if x['index'] == 'cold_hot_ratio' else x['value'] - (x['value'] * 2), axis=1)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for each category
colors = {'cold_hot_ratio': 'purple', 'cold': 'blue', 'hot': 'red', 'neutral': 'green'}

# Plot the bar plot for 'cold_hot_ratio' first
bar_width = 0.2
positions = np.arange(len(df))
ax.bar(positions, -df2[df2['index'] == 'cold_hot_ratio']['value'], color=colors['cold_hot_ratio'], label='Cold to Hot Ratio', alpha=0.5, align='center', width=0.4)

# Plot the bar plots for 'cold', 'hot', and 'neutral' categories separately
for i, col in enumerate(['cold', 'hot', 'neutral']):
    positions = np.arange(len(df)) + (i + 0.5) * bar_width - bar_width * 1.5
    ax.bar(positions, -df2[df2['index'] == col]['value'], color=colors[col], label=col, alpha=0.5, align='center', width=bar_width)

# Set the y-axis scale for other categories
ax.set_yticks([100 * x for x in [-4.5, -3, -1.5, 0, 2, 4, 6, 8]])
ax.set_yticklabels([1.5, 1, 0.5, 0, 100, 400, 600, 800])

# Set the labels for the y-axis
ax.set_ylabel('Values')

# Add legend
ax.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position

# Add horizontal line at y=100
ax.axhline(y=-300, color='red', linestyle='--')

# Invert y-axis to have group A at the top
ax.invert_yaxis()

plt.tight_layout()
plt.show()

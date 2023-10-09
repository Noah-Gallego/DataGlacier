import pandas as pd
import matplotlib.pyplot as plt

# Load the Cab Data from CSV file into a data frame
cab_data = pd.read_csv('Cab_Data.csv')

# Separate the data into Pink Cab and Yellow Cab data frames
pink_cab_data = cab_data[cab_data['Company'] == 'Pink Cab']
yellow_cab_data = cab_data[cab_data['Company'] == 'Yellow Cab']

# Calculate profit for Pink Cab rides
pink_cab_data['Profit'] = pink_cab_data['Price Charged'] - pink_cab_data['Cost of Trip']

# Calculate profit for Yellow Cab rides
yellow_cab_data['Profit'] = yellow_cab_data['Price Charged'] - yellow_cab_data['Cost of Trip']

# Create a bar chart for total profit for Pink Cab and Yellow Cab
cab_companies = ['Pink Cab', 'Yellow Cab']
total_profit = [pink_cab_data['Profit'].sum(), yellow_cab_data['Profit'].sum()]

plt.figure(figsize=(8, 5))
plt.bar(cab_companies, total_profit, color=['pink', 'yellow'])
plt.xlabel('Cab Company')
plt.ylabel('Total Profit')
plt.title('Total Profit Comparison between Pink Cab and Yellow Cab')

plt.show()

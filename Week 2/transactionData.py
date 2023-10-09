import pandas as pd

# Load the Cab Data from CSV file into a data frame
cab_data = pd.read_csv('Cab_Data.csv')

# Separate the data into Pink Cab and Yellow Cab data frames
pink_cab_data = cab_data[cab_data['Company'] == 'Pink Cab']
yellow_cab_data = cab_data[cab_data['Company'] == 'Yellow Cab']

# Verify the data by displaying the first few rows of each data frame
pink_cab_data.head()
# yellow_cab_data.head()

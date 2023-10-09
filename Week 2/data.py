# Import the pandas library
import pandas as pd

# Load Cab_Data.csv
cab_data = pd.read_csv('Cab_Data.csv')

# Load Customer_ID.csv
customer_data = pd.read_csv('Customer_ID.csv')

# Load Transaction_ID.csv
transaction_data = pd.read_csv('Transaction_ID.csv')

# Load City.csv
city_data = pd.read_csv('City.csv')

# Display the first few rows of each dataset to verify that they loaded successfully
print("Cab Data:")
print(cab_data.head())

print("\nCustomer Data:")
print(customer_data.head())

print("\nTransaction Data:")
print(transaction_data.head())

print("\nCity Data:")
print(city_data.head())

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\praja\OneDrive\Desktop\Project\NFLX.csv")
print("All Data:")
print(data)

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Sort the dataset based on high and low prices
sorted_data_high = data.sort_values(by='High', ascending=False)
sorted_data_low = data.sort_values(by="Low", ascending=True)

# Get the top 5 highest and lowest days based on high and low

top_5_high = sorted_data_high.head(5)
top_5_low = sorted_data_low.head(5)

# calculate the average high and low prices for each data
average_prices = data.groupby('Date').agg({'High': 'mean', 'Low': 'mean'}).reset_index()

# Visualize the average High and low prices
plt.figure(figsize=(20, 5))
plt.plot(average_prices['Date'], average_prices['High'], label='Average High')
plt.plot(average_prices['Date'], average_prices['Low'], label='Average Low')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Average High and Low Prices Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
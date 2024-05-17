import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Read the CSV data
df = pd.read_csv('OVM.csv')
print(df[:10].to_string())

df['Daily Change ( in % )'] = (df['Open'] - df['Close'])/ 100
print(df[:10].to_string())

# Define the starting and ending row indices (0-based indexing)
start_row = 10  # Change this to the desired starting row (e.g., 0 for the first row)
end_row = 30  # Change this to the desired ending row (exclusive)

# Select the desired rows of data
data_to_plot = df.iloc[start_row:end_row]  # Use iloc for row selection by index

# Extract date and high price columns
dates = data_to_plot['Date']
daily_change = data_to_plot['Daily Change ( in % )']
high_prices = data_to_plot['High']
open = df['Open']
high = df['High']
low = df['Low']
close = df['Close']
volume = df['Volume']
# Create the plot
plt.plot(dates, high_prices, label='High Price')
plt.plot(dates, daily_change, label='Daily Change')
plt.legend()

# Add a horizontal line at y=0.0000 to indicate the threshold
plt.axhline(y=0.0000, color='red', linestyle='--', label='Threshold')

# Customize the plot (optional)
plt.xlabel('Date')
plt.ylabel('Daily Change ( in % )')
plt.title('High Prices (Rows {} to {})'.format(start_row, end_row - 1))
plt.xticks(rotation=45)  # Rotate x-axis labels for readability if many dates

# Display the plot
plt.show()

# Scaling the features:
def z_score_scaling(data):
    mean = np.mean(data)
    std = np.std(data)
    return (data - mean) / std

print(z_score_scaling(open ))
print(z_score_scaling(close ))
print(z_score_scaling(high ))
print(z_score_scaling(low))
print(z_score_scaling(volume))

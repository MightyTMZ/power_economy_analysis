import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from datetime import datetime

# Load the data
GDP_data = pd.read_csv("./world-gdp-data.csv")
year_energy_regulator_established = pd.read_csv('./Year Regulator Establishment.csv')

# Merge the dataframes on the 'country' column
merged_df = pd.merge(GDP_data, year_energy_regulator_established, on='country')

# Convert column to numeric
merged_df['The Year Sector Regulator Established'] = pd.to_numeric(merged_df['The Year Sector Regulator Established'], errors='coerce')

# Get the current year
current_year = datetime.now().year

merged_df['years_regulator_existed'] = current_year - merged_df['The Year Sector Regulator Established']

# Plotting
plt.figure(figsize=(12, 6))

# Scatter plot of GDP vs. years the regulator has existed
plt.scatter(
    merged_df['years_regulator_existed'],
    merged_df['imfGDP'],
    alpha=0.7,
    s=merged_df['imfGDP'] / 0.5e10,  # Adjust the size scale factor as needed
    c='blue',
    edgecolors='w',  # the border colors
    linewidth=0.5
)


def currency_formatter(x, pos):

    num_billions = x/1e9

    if num_billions < 1000:
        return f'{x/1e9:.0f}B USD'  # Format as billions

    else:
        return f"{x/1e12:.0f}T USD"


plt.title('GDP vs. Years of Energy Regulator Existence')
plt.xlabel('Years Regulator Has Existed')
plt.ylabel('GDP')

plt.yscale('log')
plt.gca().yaxis.set_major_formatter(FuncFormatter(currency_formatter))

plt.grid(True)

# Show plot
plt.show()

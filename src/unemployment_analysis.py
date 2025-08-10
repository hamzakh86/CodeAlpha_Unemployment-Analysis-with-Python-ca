
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('../data/unemployment_rate_upto_11_2020.csv')

# Display basic information about the dataset
print('Dataset Info:')
df.info()

# Display the first few rows of the dataset
print('\nFirst 5 rows of the dataset:')
print(df.head())

# Display descriptive statistics
print('\nDescriptive Statistics:')
print(df.describe())

# Check for missing values
print('\nMissing Values:')
print(df.isnull().sum())

# Rename columns for easier access
df.columns = ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate', 'Region_Category', 'longitude', 'latitude']

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Convert 'Frequency' and 'Region_Category' to categorical type
df['Frequency'] = df['Frequency'].astype('category')
df['Region_Category'] = df['Region_Category'].astype('category')

# Display updated info to confirm data types
print('\nUpdated Dataset Info after type conversion:')
df.info()

# Save the cleaned data to a new CSV for further use
df.to_csv("../data/cleaned_unemployment_data.csv", index=False)
print("\nCleaned data saved to ../data/cleaned_unemployment_data.csv")
# --- Exploratory Data Analysis (EDA) and Visualization ---

# 1. Unemployment Rate Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Estimated Unemployment Rate'], kde=True)
plt.title('Distribution of Estimated Unemployment Rate')
plt.xlabel('Estimated Unemployment Rate (%)')
plt.ylabel('Frequency')
plt.savefig("../images/unemployment_rate_distribution.png")
plt.close()
print('Generated unemployment_rate_distribution.png')

# 2. Unemployment Rate by Region Category
plt.figure(figsize=(12, 7))
sns.boxplot(x='Region_Category', y='Estimated Unemployment Rate', data=df)
plt.title('Estimated Unemployment Rate by Region Category')
plt.xlabel('Region Category')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.savefig("../images/unemployment_rate_by_region_category.png")
plt.close()
print('Generated unemployment_rate_by_region_category.png')

# 3. Time Series of Unemployment Rate (Overall)
# Aggregate data by date to get national average (or sum) if needed, for now, just plot all points
plt.figure(figsize=(15, 7))
sns.lineplot(x='Date', y='Estimated Unemployment Rate', data=df, hue='Region_Category')
plt.title('Estimated Unemployment Rate Over Time by Region Category')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/unemployment_rate_time_series.png")
plt.close()
print('Generated unemployment_rate_time_series.png')

# 4. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Key Economic Indicators')
plt.savefig("../images/correlation_heatmap.png")
plt.close()
print('Generated correlation_heatmap.png')

print('\nData cleaning, exploration, and visualization complete.')



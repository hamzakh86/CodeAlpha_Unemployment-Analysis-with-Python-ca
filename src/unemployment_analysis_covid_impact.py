
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the cleaned dataset
df = pd.read_csv("../data/cleaned_unemployment_data.csv")

# Ensure 'Date' column is datetime
df["Date"] = pd.to_datetime(df["Date"])

# --- Analyze the impact of Covid-19 on unemployment rates ---

# Group by date and calculate the average unemployment rate
monthly_unemployment = df.groupby("Date")["Estimated Unemployment Rate"].mean().reset_index()

plt.figure(figsize=(15, 7))
sns.lineplot(x="Date", y="Estimated Unemployment Rate", data=monthly_unemployment)
plt.title("Average Estimated Unemployment Rate Over Time (All Regions)")
plt.xlabel("Date")
plt.ylabel("Average Estimated Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("../images/average_unemployment_rate_overall.png")
plt.close()
print("Generated average_unemployment_rate_overall.png")

# Analyze pre-COVID vs. during COVID (assuming COVID impact starts around March-April 2020)
# Define pre-COVID and during-COVID periods based on the dataset (Jan 2020 - Nov 2020)
pre_covid_df = df[df["Date"] < "2020-03-01"]
during_covid_df = df[(df["Date"] >= "2020-03-01") & (df["Date"] <= "2020-08-31")] # Peak impact period
post_peak_covid_df = df[df["Date"] > "2020-08-31"]

print("\nAverage Unemployment Rate Pre-COVID (Jan-Feb 2020):")
print(pre_covid_df.groupby("Region_Category")["Estimated Unemployment Rate"].mean())

print("\nAverage Unemployment Rate During Peak COVID (Mar-Aug 2020):")
print(during_covid_df.groupby("Region_Category")["Estimated Unemployment Rate"].mean())

print("\nAverage Unemployment Rate Post-Peak COVID (Sep-Nov 2020):")
print(post_peak_covid_df.groupby("Region_Category")["Estimated Unemployment Rate"].mean())

# --- Identify key patterns or seasonal trends in the data ---

# Monthly average unemployment rate across all regions
df["Month"] = df["Date"].dt.month_name()
monthly_avg_unemployment = df.groupby("Month")["Estimated Unemployment Rate"].mean().reindex([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x="Month", y="Estimated Unemployment Rate", data=monthly_avg_unemployment, palette="viridis")
plt.title("Average Estimated Unemployment Rate by Month (Overall)")
plt.xlabel("Month")
plt.ylabel("Average Estimated Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/monthly_unemployment_trends.png")
plt.close()
print("Generated monthly_unemployment_trends.png")

# Regional impact over time (using Plotly for interactivity)
fig = px.line(df, x="Date", y="Estimated Unemployment Rate", color="Region_Category",
              title="Estimated Unemployment Rate Over Time by Region Category (Interactive)",
              hover_data={"Region": True, "Estimated Employed": True})
fig.write_html("../images/unemployment_rate_time_series_interactive.html")
print("Generated unemployment_rate_time_series_interactive.html")

# State-wise unemployment rate during peak COVID
peak_covid_state_unemployment = during_covid_df.groupby("Region")["Estimated Unemployment Rate"].mean().reset_index()
peak_covid_state_unemployment = peak_covid_state_unemployment.sort_values(by="Estimated Unemployment Rate", ascending=False)

plt.figure(figsize=(15, 8))
sns.barplot(x="Estimated Unemployment Rate", y="Region", data=peak_covid_state_unemployment.head(10), palette="coolwarm")
plt.title("Top 10 Regions with Highest Average Unemployment Rate During Peak COVID")
plt.xlabel("Average Estimated Unemployment Rate (%)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("../images/top_10_regions_peak_covid.png")
plt.close()
print("Generated top_10_regions_peak_covid.png")

print("\nCOVID-19 impact analysis and trend identification complete.")



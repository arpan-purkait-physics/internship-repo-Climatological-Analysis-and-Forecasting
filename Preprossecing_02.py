import pandas as pd
import glob
import os

# Define the directory containing the CSV files
path = "/media/arpan/Hulk 64GB/IMD-DATA-2012-2023/tmax/"  # Change this to your actual path
all_files = glob.glob(os.path.join(path, "*.csv"))  # Get all CSV files

# List to store dataframes
dfs = []

for file in all_files:
    df = pd.read_csv(file)  # Read CSV file
    
    # Extract latitude and longitude from the second column name
    lat_lon = df.columns[1]  # The second column has lat lon
    df.columns = ["DateTime", f"{lat_lon.replace(' ', '_')}"]  # Rename columns
    
    dfs.append(df)

# Merge all dataframes on DateTime
merged_df = dfs[0]
for df in dfs[1:]:
    merged_df = pd.merge(merged_df, df, on="DateTime", how="outer")

# Save merged data
merged_df.to_csv("merged_data.csv", index=False)

print("Merged CSV saved as 'merged_data.csv'")

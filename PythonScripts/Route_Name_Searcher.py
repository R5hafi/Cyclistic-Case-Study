import pandas as pd

# Load your table
df = pd.read_csv('your_path')

# Split the 'route' column into four new columns
df[['start_lat', 'start_lng', 'end_lat', 'end_lng']] = df['route'].str.split(',', expand=True)

# Convert the new columns to float and round to 4 decimal places
for col in ['start_lat', 'start_lng', 'end_lat', 'end_lng']:
    df[col] = df[col].astype(float).round(4)

# List of paths to the 12 CSV files
csv_files = [
    'your_path/202305-divvy-tripdata.csv',
    'your_path/202306-divvy-tripdata.csv',
    'your_path/202307-divvy-tripdata.csv',
    'your_path/202308-divvy-tripdata.csv',
    'your_path/202309-divvy-tripdata.csv',
    'your_path/202310-divvy-tripdata.csv',
    'your_path/202311-divvy-tripdata.csv',
    'your_path/202312-divvy-tripdata.csv',
    'your_path/202401-divvy-tripdata.csv',
    'your_path/202402-divvy-tripdata.csv',
    'your_path/202403-divvy-tripdata.csv',
    'your_path/202404-divvy-tripdata.csv'
]

# Initialize an empty DataFrame to store the results
result = pd.DataFrame()

# Iterate over each row in your table
for index, row in df.iterrows():
    # For each row, iterate over the 12 CSV files until a match is found
    for csv_file in csv_files:
        # Load each CSV file
        csv_df = pd.read_csv(csv_file)
        
        # Round the 'start_lat', 'start_lng', 'end_lat', 'end_lng' columns to 4 decimal places
        csv_df[['start_lat', 'start_lng', 'end_lat', 'end_lng']] = csv_df[['start_lat', 'start_lng', 'end_lat', 'end_lng']].round(4)
        
        # Merge the current row of your table with the CSV file on the 'start_lat', 'start_lng', 'end_lat', 'end_lng' columns
        merged_df = pd.merge(row.to_frame().transpose(), csv_df, on=['start_lat', 'start_lng', 'end_lat', 'end_lng'], how='inner')
        
        # If a match is found, append the merged DataFrame to the result DataFrame and break the loop
        if not merged_df.empty:
            result = pd.concat([result, merged_df])
            break

# Save the result DataFrame to a new CSV file
result.to_csv('result.csv', index=False)

# Print a success message
print("The script has finished running successfully.")
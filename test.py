import pandas as pd
import glob

# Path to the directory containing your CSV files
directory_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\mangude_stats'

# Get all CSV files in the directory
files = glob.glob(directory_path + '/*.csv')

print("Files found:", files)  # Print the files found

# Initialize an empty list to store dataframes
dfs = []

# Read each CSV file and append its dataframe to the list
for file in files:
    df = pd.read_csv(file)
    print("Read", file)  # Print each file being read
    dfs.append(df)

# Concatenate all dataframes into a single dataframe
merged_df = pd.concat(dfs, ignore_index=True)

# Path to save the merged CSV file
output_file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud'


# Save the merged dataframe to a new CSV file
merged_df.to_csv(output_file_path, index=False)

print("Merged CSV file saved successfully.")


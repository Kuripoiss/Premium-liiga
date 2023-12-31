import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\merged_file.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Display unique values in the 'lõppseis' column to identify any anomalies
print(data['lõppseis'].unique())

# Splitting the 'lõppseis' column into 'koduväravad' and 'võõraväravad'
data[['koduväravad', 'võõraväravad']] = data['lõppseis'].str.split(' - ', expand=True)

# Convert the columns to numeric type (if applicable)
data['koduväravad'] = pd.to_numeric(data['koduväravad'], errors='coerce')
data['võõraväravad'] = pd.to_numeric(data['võõraväravad'], errors='coerce')

# Saving the modified DataFrame back to a new CSV file
new_file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\mangude_ajalugu.csv'  # Replace with your desired file path for the modified CSV
data.to_csv(new_file_path, index=False)
import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\merged_file.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Splitting the 'lõppseis' column into 'koduväravad' and 'võõraväravad' accurately
data[['koduväravad_temp', 'võõraväravad_temp']] = data['lõppseis'].str.split(' - ', expand=True)

# Extracting the correct scores by removing any non-numeric characters
data['koduväravad'] = data['koduväravad_temp'].str.replace(r'\D', '', regex=True)
data['võõraväravad'] = data['võõraväravad_temp'].str.replace(r'\D', '', regex=True)

# Convert the columns to integer type
data['koduväravad'] = pd.to_numeric(data['koduväravad'], errors='coerce')
data['võõraväravad'] = pd.to_numeric(data['võõraväravad'], errors='coerce')

# Drop unnecessary columns
data.drop(columns=['lõppseis', 'koduväravad_temp', 'võõraväravad_temp'], inplace=True)

# Saving the modified DataFrame back to a new CSV file
new_file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\mangude_ajalugu.csv'  # Replace with your desired file path for the modified CSV
data.to_csv(new_file_path, index=False)


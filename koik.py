import pandas as pd

file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\merged_file.csv'
data = pd.read_csv(file_path)

print(data['lõppseis'].unique())

data[['koduväravad', 'võõraväravad']] = data['lõppseis'].str.split(' - ', expand=True)

data['koduväravad'] = pd.to_numeric(data['koduväravad'], errors='coerce')
data['võõraväravad'] = pd.to_numeric(data['võõraväravad'], errors='coerce')

new_file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\mangude_ajalugu.csv'  # Replace with your desired file path for the modified CSV
data.to_csv(new_file_path, index=False)
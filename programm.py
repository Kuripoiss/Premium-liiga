import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\mangude_ajalugu.csv'  # Replace this with your CSV file path
data = pd.read_csv(file_path)

# Function to analyze team's performance in a specific year
def analyze_team_performance(year, team):
    # Filter data for the specified year and team
    filtered_data_home = data[(data['aasta'] == year) & (data['kodu'] == team)]
    filtered_data_away = data[(data['aasta'] == year) & (data['võõras'] == team)]

    # Counting games won, lost, and tied
    games_won_home = filtered_data_home[filtered_data_home['koduväravad'] > filtered_data_home['võõraväravad']]
    games_won_away = filtered_data_away[filtered_data_away['võõraväravad'] > filtered_data_away['koduväravad']]
    games_won_total = len(games_won_home) + len(games_won_away)

    games_lost_home = filtered_data_home[filtered_data_home['koduväravad'] < filtered_data_home['võõraväravad']]
    games_lost_away = filtered_data_away[filtered_data_away['võõraväravad'] < filtered_data_away['koduväravad']]
    games_lost_total = len(games_lost_home) + len(games_lost_away)

    games_tied_home = filtered_data_home[filtered_data_home['koduväravad'] == filtered_data_home['võõraväravad']]
    games_tied_away = filtered_data_away[filtered_data_away['koduväravad'] == filtered_data_away['võõraväravad']]
    games_tied_total = len(games_tied_home) + len(games_tied_away)

    # Plotting the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(['Games Won', 'Games Lost', 'Games Tied'], [games_won_total, games_lost_total, games_tied_total], color=['green', 'red', 'orange'])
    plt.title(f'{team} Performance in {year}')
    plt.xlabel('Result')
    plt.ylabel('Number of Games')
    plt.show()

# Example usage
year_input = int(input("Enter the year: "))
team_input = input("Enter the team name: ")

analyze_team_performance(year_input, team_input)



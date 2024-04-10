import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\koik_mangud\mangude_ajalugu.csv'
data = pd.read_csv(file_path)


def analyze_team_performance(year, team):

    filtered_data_home = data[(data['aasta'] == year) & (data['kodu'] == team)]
    filtered_data_away = data[(data['aasta'] == year) & (data['võõras'] == team)]


    games_won_home = filtered_data_home[filtered_data_home['koduväravad'] > filtered_data_home['võõraväravad']]
    games_won_away = filtered_data_away[filtered_data_away['võõraväravad'] > filtered_data_away['koduväravad']]
    games_won_total = len(games_won_home) + len(games_won_away)

    games_lost_home = filtered_data_home[filtered_data_home['koduväravad'] < filtered_data_home['võõraväravad']]
    games_lost_away = filtered_data_away[filtered_data_away['võõraväravad'] < filtered_data_away['koduväravad']]
    games_lost_total = len(games_lost_home) + len(games_lost_away)

    games_tied_home = filtered_data_home[filtered_data_home['koduväravad'] == filtered_data_home['võõraväravad']]
    games_tied_away = filtered_data_away[filtered_data_away['koduväravad'] == filtered_data_away['võõraväravad']]
    games_tied_total = len(games_tied_home) + len(games_tied_away)


    plt.figure(figsize=(8, 6))
    bars = plt.bar(['Võite', 'Kaotusi', 'Viike'], [games_won_total, games_lost_total, games_tied_total], color=['green', 'red', 'blue'])
    plt.title(f'{team} tulemused aastal {year}')
    plt.xlabel('')
    plt.ylabel('Mängude arv')


    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval), va='bottom', ha='center', fontsize=10)

    plt.show()


year_input = int(input("Sisestage aasta(2018-2023): "))
team_input = input("Sisestage tiimi nimi: ")

analyze_team_performance(year_input, team_input)



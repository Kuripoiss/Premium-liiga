import os
import requests
from bs4 import BeautifulSoup

def scrape_tulemused(aastaarv):
    web = "https://jalgpall.ee/voistlused/52/liigad/calendar?season=" + str(aastaarv)
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, "lxml")

    kodu = []
    lõppseis = []
    võõras = []

    mängud = soup.find_all("div", class_="event-single")
    for mäng in mängud:
        kodu.append(mäng.find("div", class_="team").get_text(strip=True))
        lõppseis.append(mäng.find("div", class_="result").get_text(strip=True))
        võõras.append(mäng.find_all("div", class_="team")[1].get_text(strip=True))

    mängude_kogu = {"kodu": kodu, "lõppseis": lõppseis, "võõras": võõras}


    filename = f'jalgpall_results_{aastaarv}.csv'
    save_dir = r'C:\Users\marte\PycharmProjects\helloworld\pythonProject\mangude_stats'
    file_path = os.path.join(save_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("kodu,lõppseis,võõras,aasta\n")
        for i in range(len(kodu)):
            file.write(f"{kodu[i]},{lõppseis[i]},{võõras[i]},{aastaarv}\n")



for year in range(2018, 2024):
    scrape_tulemused(year)

import requests
from bs4 import BeautifulSoup
mängud_url = 'https://jalgpall.ee/voistlused/52/premium-liiga'
data = requests.get(mängud_url)
soup = BeautifulSoup(data.text, "html.parser")
tiimide_tabel = soup.select("table.game-stats")[0]
lingid = tiimide_tabel.find_all("a")
lingid = [l.get("href") for l in lingid]
lingid = [l for l in lingid if "/team/" in l]

tiimide_url = [f"https://jalgpall.ee{l}" for l in lingid]
tiimi_url = tiimide_url[0]
data = requests.get(tiimi_url)

import pandas as pd

def scrape_tulemused(aastaarv):

    web = "https://jalgpall.ee/voistlused/52/liigad/calendar?season=" + str(aastaarv)
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, "lxml")

    #tiimid = ["flora", "levadia", "kalev", "paide", "nõmme-kalju", "pärnu-vaprus", "kurressaare", "narva",
              #"tartu-tammeka", "harju"]
    aastad = [2018, 2019, 2020, 2021, 2022, 2023]

    kodu = []
    lõppseis = []
    võõras = []

    mängud = soup.find_all("div", class_="event-single")
    for mäng in mängud:
        kodu.append(mäng.find("div", class_="team").get_text(strip=True))  # Home Team
        lõppseis.append(mäng.find("div", class_="result").get_text(strip=True))  # Result
        võõras.append(mäng.find_all("div", class_="team")[1].get_text(strip=True))  # Away Team


    mängude_kogu = {"kodu": kodu, "lõppseis": lõppseis, "võõras": võõras}
    df_jalgpall = pd.DataFrame(mängude_kogu)
    df_jalgpall['kodu'] = df_jalgpall['kodu'].str.strip()
    df_jalgpall['võõras'] = df_jalgpall['võõras'].str.strip()
    df_jalgpall['lõppseis'] = df_jalgpall['lõppseis'].str.strip()
    df_jalgpall["aasta"] = "2023"


    print(df_jalgpall)


scrape_tulemused(2020)

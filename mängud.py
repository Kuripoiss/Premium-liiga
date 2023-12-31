import pandas as pd
import requests
from bs4 import BeautifulSoup

web = "https://jalgpall.ee/voistlused/52/liigad/calendar?season=2023"
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
for i, mäng in enumerate(mängud):
    if i % 2 == 0:
        kodu = mäng.find("div", class_="team").get_text().strip()
        kodu.append(kodu)
    else:
        võõras = mäng.find("div", class_="team").get_text().strip()
        võõras.append(võõras)

    lõppseis = mäng.find("div", class_="result").get_text().strip()
    lõppseis.append(lõppseis)

    #kodu.append(mäng.find("div", class_="team").get_text())
    #lõppseis.append(mäng.find("div", class_="result").get_text())
    #võõras.append(mäng.find("div", class_="team").get_text())


mängude_kogu = {"kodu": kodu, "lõppseis": lõppseis, "võõras": võõras}
df_jalgpall = pd.DataFrame(mängude_kogu)
#df_jalgpall['kodu'] = df_jalgpall['kodu'].str.strip()
#df_jalgpall['võõras'] = df_jalgpall['võõras'].str.strip()
#df_jalgpall['lõppseis'] = df_jalgpall['lõppseis'].str.strip()
df_jalgpall["aasta"] = "2023"



print(df_jalgpall)


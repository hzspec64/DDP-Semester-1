from bs4 import BeautifulSoup
import requests

def jadwalSholat(url):
    contents = requests.get(url)
    response = BeautifulSoup(contents.text,"html.parser")
    data = response.find('tr', class_='table_highlight')

    sholat = {}
    i = 0

    for value in data:
        if i == 1:
            sholat['Imsyak'] = value.get_text()
        elif i == 2:
            sholat['Subuh'] = value.get_text()
        elif i == 3:
            sholat['Terbit'] = value.get_text()
        elif i == 4:
            sholat['Dhuha'] = value.get_text()
        elif i == 5:
            sholat['Zuhur'] = value.get_text()
        elif i == 6:
            sholat['Ashar'] = value.get_text()
        elif i == 7:
            sholat['Maghrib'] = value.get_text()
        elif i == 8:
            sholat['Isya'] = value.get_text()
        
        i += 1
    return sholat

url = "https://jadwalsholat.org/jadwal-sholat/monthly.php"
print(jadwalSholat(url))
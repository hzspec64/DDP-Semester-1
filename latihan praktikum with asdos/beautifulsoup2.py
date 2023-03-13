from bs4 import BeautifulSoup

htmltxt = '''
<!DOCTYPE html>
<html>
<head>
    <title>Praktikum 9 Beautiful Soup</title>
</head>
<body>
    <p class="judul">Ini adalah judul bs4</p>
    <p class="isi">Ini adalah isi body</p>
    <p class="footer">Ini adalah isi body</p>
</body>
</html>
'''

soup = BeautifulSoup(htmltxt,"html.parser")

judul = soup.find('p', class_="judul").text
print(judul)
print("-----------------------------")

paragraf = soup.find('p', class_="isi").text
print(paragraf)
print("-----------------------------")

all_paragraf = soup.find_all('p')
print(all_paragraf)
from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><p>Ini cara menggunakan bs4</p></html>", "html.parser")
print("-----------------------------")
print(soup)
print("-----------------------------")

soup = BeautifulSoup("<html><p>Ini cara menggunakan bs4 lxml</p></html>", "lxml")
print("-----------------------------")
print(soup)
print("-----------------------------")

soup = BeautifulSoup("<html><p>Ini cara menggunakan bs4 xml</p></html>", "xml")
print("-----------------------------")
print(soup)
print("-----------------------------")

soup = BeautifulSoup("<html><p>Ini cara menggunakan bs4 html5lib</p></html>", "html5lib").text 
print("-----------------------------")
print(soup)
print("-----------------------------")
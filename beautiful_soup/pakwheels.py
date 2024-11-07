import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"
html = requests.get(url)
 
soup = BeautifulSoup(html.text, 'html.parser')

result = soup.find(id="mp-tfa-img")
page_title = result.find_all(class_="thumbinner mp-thumb")

for link in soup.find_all("img"):
    print(link.get("src"))
print(link.get_text())
from bs4 import BeautifulSoup
import requests

url = "https://www.skiresort.info/ski-resort"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

rows = soup.find_all("div", class_="row")

for row in rows:
    h3_tag = row.find("a", class_="h3")
    if h3_tag:
        a_tag = h3_tag.find('a')
        if a_tag:
            name = a_tag.text.strip()  # Resort name
            link = a_tag.get("href")   # Relative URL like: /ski-resort/carezza/
            
            if link and link.startswith("/ski-resort/"):
                full_url = "https://www.skiresort.info" + link
                print(f"resort name : {name}")
                print(f"resort url  : {full_url}")

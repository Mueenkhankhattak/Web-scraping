import requests
import os

print("Saving to:", os.getcwd())


url = "https://imgs.xkcd.com/comics/python.png"
r = requests.get(url)

if r.status_code == 200:
    with open("comics.png" , 'wb') as f:
        f.write(r.content)

else:
    print("Failed to dowload image:" , r.status_code)
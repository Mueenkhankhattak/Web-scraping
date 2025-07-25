import requests

url = "https://imgs.xkcd.com/comics/python.png"

response = requests.get(url)

print(response.status_code) # 200
print(response.headers)
print(response.content) # Binary content of the image
print(response.text) # Text content of the r
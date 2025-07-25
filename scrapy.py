from bs4 import BeautifulSoup
import requests
import csv

csv_file = open("Qoutes.csv" , 'w' ,newline='' ,encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote' , 'Author' ,'Tags'])

for page in range(1,11):

    url =  f"https://quotes.toscrape.com/page/{page}/"

    source = requests.get(url).text

    soup = BeautifulSoup(source , 'lxml')

    qoutes = soup.find_all("div" , class_='quote')

    for qoute in qoutes:
        text = qoute.find("span"  ,class_='text').text.strip()
        
        auth = qoute.find('small' ,class_='author').text.strip()
        tag = [q.text.strip() for q in qoute.find_all("a" , class_='tag')]
        csv_writer.writerow([text , auth ,','.join(tag)])


        print(f"Quote is : {text}")
        print(f'auther name is : {auth}')
        print(f"Tags : {' ,'.join(tag)}")


csv_file.close()
print("Csv file Created")

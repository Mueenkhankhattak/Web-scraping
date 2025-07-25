from bs4 import BeautifulSoup
import requests
url = "https://techcrunch.com/2025/07/24/ai-companions-a-threat-to-love-or-an-evolution-of-it/"
source = requests.get(url).text

soup = BeautifulSoup(source , 'lxml')

title = soup.title
print(title.string)
   
print("'''''''''''''..................................''''''''''''''''''")
# title of the article

#find the social media
social_link = soup.find("div" ,class_="wp-block-tc23-author-card-social")
if social_link: 
    links =[link.get("href") for link in social_link.find_all('a')]
    print("author socail linkad :" , links)

else:
    print("Author have no social links")

#now lets find the embed vedio 
print(".......................................................................")

vedio = soup.find("iframe")
if vedio:
    print("Embeded vedio" , vedio.get("src"))

else:
    print("No vedio found")


print("""""""""""....................................................""""""""""""""")
#find the auth bio 
auth_bio = soup.find("div" ,class_="wp-block-tc23-author-card-bio").p.text
print(auth_bio)
# print(soup.prettify())for link in social_link.
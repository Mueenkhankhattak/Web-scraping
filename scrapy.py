from bs4 import BeautifulSoup
import requests
import csv
import logging

csv_file = open("Quotes.csv" , 'w' ,newline='' ,encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote' , 'Author' ,'Tags'])

class ScrapeCode:
    def __init__(self ,url):
        self.url = url
        self.html = None
        self.soup = None
        self.quotes = None

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status
            self.html =  response.text

            logging.info(f'Successfully fetch the page:')
        except Exception as e:
            logging.error(f"Error while Fetching Page: , {e}")


    def parse_html(self):
        try:
            if self.html is None:
                logging.info("Error first run the fetch_html() :")
            else:
                self.soup = BeautifulSoup(self.html , "lxml")
                logging.info("successfully parse the html page")

        except Exception as e:
            logging.info(f"Error while parsing the page : {e}")


    def fetch_quote_(self):
        try:
            self.quotes = self.soup.find_all("div" ,class_="quote")
            if self.quotes is None:
                logging.warning("No Qoute found")
            
            else:
                for quote in self.quotes:
                    text = quote.find("span" ,class_="text").text.strip()
                    author = quote.find("small", class_="author").text.strip()
                    tags = [tag.text.strip() for tag in quote.find_all("a", class_="tag")]
                    logging.info(f"Quote: {text} | Author: {author} | Tags: {tags}")
                    csv_writer.writerow([text, author, ", ".join(tags)])

        except Exception as e:
            logging.error(f"Error while fetching quotes: {e}")
                   


if __name__ == "__main__":

    for page in range(1, 11):
        url = f"https://quotes.toscrape.com/page/{page}/"
        scrape = ScrapeCode(url)
        scrape.fetch_html()
        scrape.parse_html()
        scrape.fetch_quote_()

    csv_file.close()
    print("Csv file Created")

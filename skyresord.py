from bs4 import BeautifulSoup
import requests
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SkyResort:

    def __init__(self,url):
        self.url = url
        self.html = None
        self.soup = None
        self.resort_link = []

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.html = response.text
            logging.info(f"Successfully fetched the html")
        except Exception as e:
            logging.error(f"Error while fetching the html page : {e}")

    def parse_html(self):
        try:
            if self.html is None:
                logging.warning(f" Error: run the fetch_html()")

            else:
                self.soup = BeautifulSoup(self.html , 'lxml')
                
                logging.info(f"Successfully parse the html ")
            
        except Exception as e:
            logging.error(f"Error while parsing the html : {e}")

    def grab_urls(self):
        try:
            if self.soup is None:
                logging.warning(f'Error in self.soup')
            else:
                rows = self.soup.find_all("div" ,class_="row" )
                for row in rows:
                    h3_tag = row.find("a" , class_='h3')
                    if h3_tag:
                        relative_url = h3_tag.get('href')
                        full_url = f"https://www.skiresort.info{relative_url}"
                        self.resort_link.append(full_url)
                        resort_name = h3_tag.text.strip()
                        logging.info(f"Found Resort: {resort_name}, Link: {full_url}")
        except Exception as e:
            logging.error(f" Error while grabbing URLs: {e}")

    def extarct_table(self):
        if not self.resort_link:
            logging.warning("⚠️ No resort links found")
            return
        try:
            for link in self.resort_link:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'lxml')
                describtion = soup.find_all('div', class_="detail-links")
                for des in describtion:
                    des.find("div" , class_="description")

                    table = des.find("table" , class_="info-table")
                    if table:
                        print(f"\nTable data from: {link}")
                        rows = table.find_all('tr')
                        for row in rows:
                            cells = row.find_all(["td", "th"])
                            row_data = [cell.text.strip() for cell in cells]
                            print(row_data)
                    else:
                        logging.info(f"No table found in {link}")
        except Exception as e:
            logging.error(f"Error while extracting table from {link}: {e}")

   



if __name__ == "__main__":

    url = "https://www.skiresort.info/ski-resort/"
    scrapper = SkyResort(url)
    scrapper.fetch_html()
    scrapper.parse_html()
    scrapper. grab_urls()
    scrapper.extarct_table()
    

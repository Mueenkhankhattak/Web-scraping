from bs4 import BeautifulSoup
import requests
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SkyResord:

    def __init__(self,url):
        self.url = url
        self.html = None
        self.soup = None

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.html = response.text
            logging.info(f"Successfully fetch the html")
        except Exception as e:
            logging.error(f"Error while fetching the html page : {e}")

    def parse_html(self):
        try:
            if self.html is None:
                logging.warning(f"Error first run the fetch_html()")

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
                        resort_link = h3_tag['href']
                        resort_name = h3_tag.text.strip()
                        logging.info(f"resord link: {resort_link}, resord_name: {resort_name} ")

        except Exception as e:
            logging.error(f"Error while fetching the urls, {e}")

    def grab_oprating_time(self):
        try:
            if self.soup is None:
                logging.warning('Error in self.soup while fetching operating time')
                return
            describtion = self.soup.find_all('div', class_='detail-links')
            logging.info(f"Found {len(describtion)} 'detail-links' divs")
            for des in describtion:
                h3_tag = des.find('h3', class_='label h5')
                if h3_tag:
                    h3_text = h3_tag.text.strip()
                else:
                    h3_text = None
                table = des.find('table', class_='info-table')
                if table:
                    operating_time = table.find(id='selSeason')
                    operating_time2 = table.find(id='selOperationtimes')
                    operating_time3 = table.find(id='selGenseason')
                    note = table.find('td', colspan='2')
                    logging.info(
                        f"h3: {h3_text} | "
                        f"operating_time: {operating_time.text.strip() if operating_time else 'N/A'} | "
                        f"operating_time2: {operating_time2.text.strip() if operating_time2 else 'N/A'} | "
                        f"operating_time3: {operating_time3.text.strip() if operating_time3 else 'N/A'} | "
                        f"note: {note.text.strip() if note else 'N/A'}"
                    )
        except Exception as e:
            logging.error(f"Error while fetching operating time: {e}")
    

    def grab_main_link(self):
        try:
            detail_link = self.soup.find_all("div", class_="detail-links")
            logging.info(f"Found {len(detail_link)} 'detail-links' divs for main link")
            for link in detail_link:
                name_tag_div = link.find("div", class_="label h5")
                name_tag = name_tag_div.text.strip() if name_tag_div else None
                main_link = link.find('div', class_="description")
                if main_link:
                    main_website_links = [a.get('href') for a in main_link.find_all('a')]
                    logging.info(f"Resort: {name_tag} | Website Link(s): {main_website_links}")
        except Exception as e:
            logging.error(f'Error while grabbing the main website link: {e}')





if __name__ == "__main__":

    url = "https://www.skiresort.info/ski-resort/"
    scrapper = SkyResord(url)
    scrapper.fetch_html()
    scrapper.parse_html()
    scrapper. grab_urls()
    scrapper.grab_oprating_time()
    scrapper.grab_main_link()

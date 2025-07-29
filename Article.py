from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Wbscraper:
    def __init__(self ,url):

        self.url = url
        self.html = None
        self.soup = None

    def fetch_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.html = response.text
            logging.info("successfully fetched the html page")

        except Exception as e:
            logging.error(f"Error: while fetching html page : {e}")


    def parse_html(self):
        try:
            if self.html is None:
                logging.warning("Erorr: run fetch_html() first")

            else:
                self.soup = BeautifulSoup(self.html , 'lxml')
                logging.info("succesfuly parse the html")

        except Exception as e:
            logging.error(f'Error While parsing the html : {e}')


    # title of the article
    def fetch_title(self):
        try:
            title = self.soup.title.string if self.soup.title else 'not title found'
            logging.info(f'Title: {title}')
        except Exception as e:
            logging.info(f"Error while fecthing the title : {e}")


    # find the social media
    def fetch_social_link(self):
        if self.soup is None:
            logging.warning("Error: run parse_html() first")
            return
        try:
            social_link = self.soup.find("div", class_="wp-block-tc23-author-card-social")
            if social_link:
                links = [link.get("href") for link in social_link.find_all('a')]
                logging.info(f"Author social links: {links}")
            else:
                logging.info("Author has no social links.")
        except Exception as e:
            logging.error(f"No social media found error: {e}")

    # now lets find the embed video
    def fetch_video(self):
        if self.soup is None:
            logging.warning("Error: run parse_html() first")
            return
        try:
            video = self.soup.find("iframe")
            if video and video.get('src'):
                logging.info(f"Embedded video: {video.get('src')}")
            else:
                logging.info("No video found.")
        except Exception as e:
            logging.error(f"No video found: {e}")

    def fetch_author_bio(self):
        if self.soup is None:
            logging.warning("Error: run parse_html() first")
            return
        try:
            bio_div = self.soup.find("div", class_="wp-block-tc23-author-card-bio")
            if bio_div and bio_div.p:
                auth_bio = bio_div.p.text
                logging.info(f"Author bio: {auth_bio}")
            else:
                logging.info("No author bio found.")
        except Exception as e:
            logging.error(f"No paragraph found: {e}")

if __name__ == "__main__":

    url = "https://techcrunch.com/2025/07/24/ai-companions-a-threat-to-love-or-an-evolution-of-it/"

    scraper = Wbscraper(url)
    scraper.fetch_html()
    scraper.parse_html()
    scraper.fetch_title()
    scraper.fetch_social_link()
    scraper.fetch_video()
    scraper.fetch_author_bio()



import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="WebScrapper")
parser.add_argument("-s", "--site", help="Site alvo", required=True)
args = parser.parse_args()
site = args.site

def Scrapper (url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  urls = [a["href"] for a in soup.find_all("a", href=True)]
  
  return urls

urls = Scrapper(site)
for url in urls:
  print(url)
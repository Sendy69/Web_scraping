import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "html.parser")
    title = bs.h1
    return title

title = scrape_title(url="https://www.blogdumoderateur.com/tools/tech/web-scraping/")
print(title)
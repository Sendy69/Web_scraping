import re
import requests
from bs4 import BeautifulSoup

# this function allows to retrieve all https pages of the web site
def get_all_pages():
    page_number = 1
    list_of_urls = []
    for i in range(104):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page_number}"
        list_of_urls.append(i)
        page_number +=1
    return list_of_urls

#this function allows to scrap a page
def get_lawyer(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "html.parser")
    #here we retrieve all content of the page but only div of lawyer
    avocats = bs.find_all("div", class_="callout secondary annuaire-single")
    
    for avocat in avocats:

        nom = avocat.find("h3", class_="nom-prenom").text.strip()
        adresse = avocat.find("span", class_= "adresse").text.strip()
        adresse_final = re.sub(r"\s+", " ", adresse)
        telephone = avocat.find("span", class_= "telephone").text.strip()
        mail = avocat.find("span", class_= "email").a.text.strip()

        chemin = r"C:\Users\sandr\Documents\Learning\Web scraping\Web_scraping"
        
        with open(chemin, "a") as f:
            f.write(f"{nom}\n")
            f.write(f"{adresse_final}\n")
            f.write(f"{telephone}\n")
            f.write(f"{mail}\n\n")
        
#this function allows to scrap data on each page
def get_all_lawyers():
    pages = get_all_pages()

    for page in pages:
        get_lawyer(page)
        print(f"On scrape {page}")

get_all_lawyers()
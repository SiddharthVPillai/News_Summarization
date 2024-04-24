from bs4 import BeautifulSoup
import requests

def scrape(url):
    if url.strip() == "":
        return ""  # Return an empty string for placeholder URLs
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    page = requests.get(url,headers=headers).text
    soup = BeautifulSoup(page,'lxml')
    txt = " "
    for i in soup.find_all('p',class_="paragraph inline-placeholder"):
        txt+=i.text.strip()
    return txt

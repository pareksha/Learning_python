import urllib.request
from bs4 import BeautifulSoup as soup

url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=laptops"

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(url)
page_html = response.read()
response.close()

page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div",{"class" : "s-item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "Full Name,Brand Name,Rating,Price\n"
f.write(headers)


for container in containers:
    name_detail = container.h2["data-attribute"]

    item_name = container.findAll("span",{"class" : "a-size-small a-color-secondary"})
    name = item_name[1].text

    stars = container.findAll("span",{"class" : "a-icon-alt"})
    if(len(stars)==2):
        star = stars[1].text
        rating = star[0:3]
    else:
        rating = "-"

    p = container.findAll("span",{"class" : "a-size-base a-color-price s-price a-text-bold"})
    price = p[0].text.strip()


    f.write(name_detail.replace(",",";")+","+name+","+rating+","+price.replace(",","")+"\n")

f.close()

import urllib.request
from bs4 import BeautifulSoup

file_name = "mobiles.csv"
f = open(file_name,"w")

headings = "Name;Screen Size;Camera;RAM;Battery;Price\n"
f.write(headings)


for i in range(1,31):

    url = "http://pricebaba.com/mobile/pricelist/4g-phones-in-india?page={}".format(i)


    req = urllib.request.Request(url , headers = {"User-Agent" : "Mozilla/5.0"})


    client = urllib.request.urlopen(req)
    html_page = client.read()
    client.close()

    page_soup = BeautifulSoup(html_page, "html.parser")

    containers = page_soup.findAll("div" , {"class" : "grid__item lap-and-up-3-12 palm-12-12 grid__item--prdp"})

    for container in containers:
        name = container.findAll("div" , {"class" : "prdp-ttl"})[0].text

        li = container.findAll("li")

        if(len(li)>>1):

            screen_size = container.findAll("li")[0].text
            camera = container.findAll("li")[1].text
            ram = container.findAll("li")[2].text


            if (len(li)==4):
                battery = li[3].text
            else:
                battery = "-"

        if(len(li) == 1):
            screen_size = container.findAll("li")[0].text

        price = container.findAll("div" , {"class" : "prdp-prc price"})[0].text[1:11]

        f.write(name+';'+screen_size+';'+camera+';'+ram+';'+battery+';'+price+'\n')

f.close()

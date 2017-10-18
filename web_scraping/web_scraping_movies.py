from urllib.request import urlopen
from bs4 import BeautifulSoup

filename = "movies.csv"
opened = open(filename,"w")
headings = "Name;Rating;Release\n"
opened.write(headings)


for i in range(2,90):

    url = "http://www.desimartini.com/hollywood-latest.htm?page={}&gclid=Cj0KCQjw1JbPBRCrARIsAOKj2Pkd11uNL-GWq_MIitfydrS98IOMQxMbSNs5LBnnI4HJ8PheQMyV8gcaAo9nEALw_wcB".format(i)
    client = urlopen(url)
    page_html = client.read()
    client.close()



    page_soup = BeautifulSoup(page_html,"html.parser")

    containers = page_soup.findAll("div", {"class" : "col-lg-6 col-md-6 col-sm-6 col-xs-6"})

    for container in containers[0:11]:
        name = container.div.div.div.h3.text.strip()

        rating = container.findAll("div" ,{"class" : "overlay-cont"})[0].div.text.strip()
        release = container.p.text.strip()

        opened.write(name.replace(';','|')+';'+rating.replace(';','|')+';'+release.replace(';','|')+';'+'\n')

opened.close()

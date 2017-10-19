from urllib.request import urlopen
from bs4 import BeautifulSoup


filename = "ngo_list.csv"
f = open(filename , "w")
f.write("Profile ID;Organisation;Location;Work Category\n")

for i in range(0,414):
    url = "http://karmayog.in/ngo/home?field_name_of_organization_value=&field_location_tid=All&field_location_tid_1=All&field_location_tid_2=All&field_work_category_tid=All&items_per_page=50&page={}".format(i)

    client = urlopen(url)
    page_html = client.read()
    client.close()

    page_soup = BeautifulSoup(page_html, "html.parser")

    containers = page_soup.tbody.findAll("tr")

    for container in containers:
        profile_id = container.findAll("td", {"class" : "views-field views-field-pid"})[0].text.strip()
        organisation = container.findAll("td", {"class" : "views-field views-field-field-name-of-organization"})[0].text.strip()
        location = container.findAll("td", {"class" : "views-field views-field-field-location"})[0].text.strip()
        work_category = container.findAll("td", {"class" : "views-field views-field-field-work-category"})[0].text.strip().replace(';',' , ')

        f.write(profile_id+';'+organisation+';'+location+';'+work_category.replace('\n',' , ')+'\n')

f.close()

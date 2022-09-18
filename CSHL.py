from bs4 import BeautifulSoup
import html5lib
import requests
import csv

f = csv.writer(open("CSHL.csv", "w"))
f.writerow(["tags"])

pages = list(range(1, 66+1))

for page in pages:
    url = "http://libgallery.cshl.edu/items/browse/" + str(page) + "?collection=9"
    r = requests.get(url)
    text_html = r.text
    soup = BeautifulSoup(text_html, features="html5lib")
    tags = soup.find_all('div', 'tags')
    for tag in tags:
        tag_final = tag.a.get_text()
        f.writerow([tag_final])
        print(tag_final)

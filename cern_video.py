from bs4 import BeautifulSoup
import html5lib
import requests
import csv
f = csv.writer(open("cern1.csv", "w"))
f.writerow(["tags"])

#ids = list(range(2295150, 2296469+1))
ids = list(range(2781035, 2791010+1))

for id in ids:
    url = "https://videos.cern.ch/record/" + str(id)
    r = requests.get(url)
    text_html = r.text
    soup = BeautifulSoup(text_html, features="html5lib")
    tags = soup.find_all('invenio-search','search-endpoint'==True)
    for tag in tags:
        tag.div.decompose()
        tag1 = tag.get("search-endpoint")
        tag2 = str(tag1)
        tag_result = tag2.replace("/api/records/?size=3&sort=mostrecent&q=category:", "")
        f.writerow([tag_result])
        print(tag_result)
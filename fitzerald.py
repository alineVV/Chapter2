from bs4 import BeautifulSoup
import html5lib
import requests
import csv
f = csv.writer(open("fitzerald.csv", "w"))
f.writerow(["tags"])

ids = list(range(372, 2390+1))

for id in ids:
    url = "https://digitalarchive.rds.ie/items/show/" + str(id)
    r = requests.get(url)
    text_html = r.text
    soup = BeautifulSoup(text_html, features="html5lib")
    tags = soup.find_all('div', id = "dublin-core-subject")
    for tag in tags:
        tags2 = tag.find_all('a')
        for tag2 in tags2:
            final_tag = tag2.text.strip()
            print(final_tag)
            f.writerow([final_tag])




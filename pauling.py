from bs4 import BeautifulSoup
import html5lib
import requests
import csv
import string

f = csv.writer(open("pauling.csv", "w"))
f.writerow(["tags"])

alphabet_string = string.ascii_uppercase
alphabet = list(alphabet_string)

for letter in alphabet:
    url = "http://scarc.library.oregonstate.edu/coll/pauling/rnb/index/index" + letter + ".html"
    r = requests.get(url)
    text_html = r.text
    soup = BeautifulSoup(text_html, features="html5lib")
    for x in soup.findAll("td"):
        if "colspan" in x.attrs:
            result = x.text.strip()
            f.writerow([result])



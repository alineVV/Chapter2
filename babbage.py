import json
import requests
import csv
from nltk import flatten

f = csv.writer(open("babbage.csv", "w"))
f.writerow(["tags"])
list1 = []
url = "https://umedia.lib.umn.edu/search.json?facets[contributing_organization_name_s][]=University+of+Minnesota+Libraries%2C+Charles+Babbage+Institute.&rows=3500"
resp = requests.get(url)
resp1 = resp.json()
for r in resp1:
    subject = r.get("subject_ss")
    list1.append(subject)

list_flattened = flatten(list1)
result = [i for n, i in enumerate(list_flattened) if i not in list_flattened[:n]]
for r in result:
    f.writerow([r])

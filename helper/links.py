import json
import os

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://docs.streamlit.io"

r = requests.get(f"{BASE_URL}/library/api-reference")
soup = BeautifulSoup(r.content, "html.parser")

links = {}

for section in soup.select("div.content section.tileContainer_Container__KCC27")[:-1]:
    for a in section.select("a.refCard_Container__cRE_M"):
        link = f"{BASE_URL}{a.attrs['href']}"
        name = f"{link.split('/')[-1]} - {a.select_one('h4').text}"

        links[name] = link

with open(os.path.join("..", "links.json"), "w") as file:
    json.dump(links, file, indent=2, sort_keys=False)

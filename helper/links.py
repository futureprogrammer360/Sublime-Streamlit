import json
import os

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://docs.streamlit.io"

r = requests.get(f"{BASE_URL}/library/api-reference")
soup = BeautifulSoup(r.content, "html.parser")

links = {}

for section in soup.select("div.content section"):
    if (p := section.select_one("div div p")) is not None and p.text == "Third-party components":
        continue
    for a in section.select("a.refCard_Container__LoksC"):
        link = f"{BASE_URL}{a.attrs['href']}"
        name = f"{link.split('/')[-1]} - {a.select_one('h4').text}"

        links[name] = link

with open(os.path.join("..", "links.json"), "w") as file:
    json.dump(links, file, indent=2, sort_keys=False)

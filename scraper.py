#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup 

URL = requests.get("https://www.bbc.co.uk/news")

soup = BeautifulSoup(URL.text, 'html.parser')


articles = soup.select(".gs-c-promo-heading__title")

# print("articles contains {} elements\n".format(len(articles)))

for article in articles:
	print(article.get_text())
	

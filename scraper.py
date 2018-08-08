#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup 

URL = requests.get("https://www.bbc.co.uk/news")

soup = BeautifulSoup(URL.text, 'html.parser')


sub_articles = soup.select(".gs-c-promo-heading__title")

# b vprint("sub_articles contains {} elements\n".format(len(sub_articles)))

for article in sub_articles:
	print(article.get_text())
	

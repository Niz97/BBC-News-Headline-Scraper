#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup 

URL = requests.get("https://www.bbc.co.uk/news")

soup = BeautifulSoup(URL.text, 'html.parser')


articles = soup.select(".gs-c-promo-heading__title")

# print("articles contains {} elements\n".format(len(articles)))

# for article in articles:
# 	print(article.get_text())
	
def print_list(list):
	data = list
	for element in data:
		print(element)

def get_element_text(list_of_elements, n):
	number_of_elements = n
	elements = list_of_elements
	element_text = []
	for i in range(number_of_elements):
		element_text.append(elements[i].get_text())

	return element_text

print_list(get_element_text(articles, 6))

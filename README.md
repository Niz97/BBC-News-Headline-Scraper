# BBC-News-Headline-Scraper
# Python web scraper to pull information from the BBC home page


Class | Content
------|--------
Headline article | gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text
Headline of every article on page | gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text


# TO DO
Find the div containing each article - class="gel-wrap" 
--------------------------------------------------------	
* Find the headline article
  - [x] Get the headline from that article
    - [x] Remove HTML and white space
      - [x] Print headline

* Get all other headlines from other articles
  - [x] Remove HTML and white space
    - [x] Print article headline

* Choose how many headlines are displayed
  - [x] Implement function to print x number of headlines
  - [ ] Choose this via a cmd menu system or passing command line argument
  
* Give the option to print a small passage from the article
  - [ ] Find the element that contains a brief summary of the article
   - [ ] Pull only the the summaries of articles requested


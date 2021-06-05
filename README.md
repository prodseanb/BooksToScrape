# BooksToScrape
Scraping exercise from [books.toscrape.com](https://books.toscrape.com/index.html)  
## Requirements
To run this project, you'll need to install [BeautifulSoup](https://pypi.org/project/beautifulsoup4/).
```bash
pip3 install beautifulsoup4
```
## Clone repository and execute
```bash
git clone https://github.com/prodseanb/BooksToScrape.git
python3 scraper_5.py
```
## urls
```python

#url dictionary, value to append to URL = f"https://books.toscrape.com/catalogue/category/books/{}/index.html"
urls = {
	
		"Travel": "travel_2",
		"Mystery": "mystery_3",
		"Historical Fiction": "historical-fiction_4",
		"Sequential Art": "sequential-art_5",
		"Classics": "classics_6",
...
```
for key, value in urls<br />
value = appends to URL to query the genre.
## Objective
This program scrapes every section of placeholder data from [books.toscrape.com](https://books.toscrape.com/index.html)

### License
[GNU](https://gist.github.com/nicolasdao/a7adda51f2f185e8d2700e1573d8a633#gpl-license-aka-gnu-general-public-license-v30)

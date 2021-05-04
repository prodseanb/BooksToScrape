##Scrape book titles, prices, availability status, and categories
import requests
from bs4 import BeautifulSoup


URL = "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
#scrape the categories
section = []
for ul in soup.findAll('ul', class_="nav"):
	for li in ul.findAll('li'):
		for inner_ul in li.findAll('ul'):
			for a in inner_ul.findAll('a'):
				sections = ((a).get_text()\
					.strip(' \n'))
				section.append(sections)

#url dictionary, value to append to URL = f"https://books.toscrape.com/catalogue/category/books/{}/index.html"
urls = {
	
		"Travel": "travel_2",
		"Mystery": "mystery_3",
		"Historical Fiction": "historical-fiction_4",
		"Sequential Art": "sequential-art_5",
		"Classics": "classics_6",
		"Philosophy": "philosophy_7",
		"Romance": "romance_8",
		"Womens Fiction": "womens-fiction_9",
		"Fiction": "fiction_10",
		"Childrens": "childrens_11",
		"Religion": "religion_12",
		"Nonfiction": "nonfiction_13",
		"Music": "music_14",
		"Default": "default_15",
		"Science Fiction": "science-fiction_16",
		"Sports and Games": "sports-and-games_17",
		"Add a comment": "add-a-comment_18",
		"Fantasy": "fantasy_19",
		"New Adult": "new-adult_20",
		"Young Adult": "young-adult_21",
		"Science": "science_22",
		"Poetry": "poetry_23",
		"Paranormal": "paranormal_24",
		"Art": "art_25",
		"Psychology": "psychology_26",
		"Autobiography": "autobiography_27",
		"Parenting": "parenting_28",
		"Adult Fiction": "adult-fiction_29",
		"Humor": "humor_30",
		"Horror": "horror_31",
		"History": "history_32",
		"Food and Drink": "food-and-drink_33",
		"Christian Fiction": "christian-fiction_34",
		"Business": "business_35",
		"Biography": "biography_36",
		"Thriller": "thriller_37",
		"Contemporary": "contemporary_38",
		"Spirituality": "spirituality_39",
		"Academic": "academic_40",
		"Self Help": "self-help_41",
		"Historical": "historical_42",
		"Christian": "christian_43",
		"Suspense": "suspense_44",
		"Short Stories": "short-stories_45",
		"Novels": "novels_46",
		"Health": "health_47",
		"Politics": "politics_48",
		"Cultural": "cultural_49",
		"Erotica": "erotica_50",
		"Crime": "crime_51",
}

print(section)
print('\n')




# scrape the book title
##problem: print the whole title --solved
def foo():
	title = []
	for h3 in soup.find_all('h3'):
		for a in h3.find_all('a'):
			title_count = (a.get('title'))
			title.append(title_count)

	# scrape the price
	price = []
	for p_count in soup.findAll('p', class_="price_color"):
		price_count = ((p_count).get_text().replace('Â',''))

		price.append(price_count)

	#scrape the stock availability status
	stock = []
	for s_count in soup.findAll('p', class_='instock'):

	##problem: need to print only the "In stock" occurence --solved
		stock_count = ((s_count).get_text().strip(' \n'))
		stock.append(stock_count)


	category = soup.find('h1').get_text()
	print('\n' + 'Books in: ' + category + '\n')

	for index, (val1, val2, val3) in \
	enumerate(zip(title, price, stock)):
		print(val1 + "\n" + val2 + "\n" + val3 + "\n") 




while True:
	try:
		query = input('Pick a category: ') 
		if query in urls:
			href = (urls[query])
			#print(href)
			####problem -- href prints the entire dict --solved
			###problem -- case sensitive dictionary, input has to match the letter case to yield
			URL = f"https://books.toscrape.com/catalogue/category/books/{href}/index.html"
			page = requests.get(URL)
			soup = BeautifulSoup(page.text, 'html.parser')
			foo()
			break
		else:
			raise Exception
	except Exception as e:
		print('Category not found. Please try again. NOTE: Case sensitive')
import requests
from bs4 import BeautifulSoup
import os


#Pour récupérer l'ensemble des catégorie (problème index de la liste car str et non int/slice)

url = 'http://books.toscrape.com/index.html'
ctgLinks = []
bookLinks = []
bookData = {}

def get_categories(url):
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.text, 'html.parser')
		menu = soup.find('ul', {'class': 'nav nav-list'})
		categories = menu.findAll('a')
		for categorie in categories:
			ctg = 'http://books.toscrape.com/' + categorie['href']
			ctgLinks.append(ctg)
	return ctgLinks[1:]

#Pour récupérer l'ensemble des livres d'une catégorie (terminé)
def get_book_urls(ctglinks):
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.text, 'lxml')
		articles = soup.findAll('article')
		for article in articles:
			a = article.find('a')['href'].replace('../../..','http://books.toscrape.com/catalogue')
			bookLinks.append(a)
			next = soup.find('li', {'class': 'next'})	
			if next:
				link = next.find('a')['href']
				suite = url.replace('index.html',link)
				bookLinks.append(get_book_urls(suite))
	return bookLinks

#Pour récuperer toutes les informations d'un livre (terminé)
def get_book_data(bookLinks):
	response = requests.get(bookLinks)
	if response.ok:
		soup = BeautifulSoup(response.text, 'html.parser')
		trs = soup.findAll('tr')
		bookData['url'] = url
		bookData['upc'] = trs[0].find('td').text
		bookData['title'] = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1').text
		bookData['price_including_tax'] = trs[3].find('td').text
		bookData['price_excluding_tax'] = trs[2].find('td').text
		bookData['number_available'] = trs[5].find('td').text	
		bookData['product_description'] = soup.find('meta', {'name': 'description'})['content']
		bookData['category'] = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')[2].text
		bookData['review_rating'] = soup.find('p', {'class': 'star-rating'})['class'][1]
		pic = soup.find('img')['src']
		bookData['image_url'] = pic.replace('../..', 'http://books.toscrape.com')
	return bookData

#Pour télécharger la première couverture du livre (comment creer les fichiers dans le dossier pictureData)
try:
	os.mkdir('pictureData')

get_categories(url)
for link in ctgLinks:
	link.get_book_urls(ctglinks)
	b = ctglinks.replace('http://books.toscrape.com/catalogue/category/books/','').replace('/index.html','')
	os.mkdir(b)
	file = open(b/'bookData.csv', 'w+')
	file.write('product_page_url, universal_ product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url, \n')		
	for book in bookLinks:
		book.get_book_data(bookLinks)
		for info in bookData:
			file.write(str(bookLinks)+','+str(bookData['upc'])+','+bookData['title']+','+str(bookData['price_including_tax'])+','+str(bookData['price_excluding_tax'])+','+str(bookData['number_available'])+','+bookData['product_description'].replace('\n','')+','+bookData['category']+','+bookData['review_rating']+','+str(bookData['image_url']+"\n"))
			file.close()	

for photo in bookData['image_url']:
	picture = requests.get(bookData['image_url'])
	image =open(pictureData/bookData['title']+'.png', "wb")
	image.write(picture.content)
	picture.close()
import requests
from bs4 import BeautifulSoup
import os

"""
#Pour récupérer l'ensemble des catégorie (problème index de la liste car str et non int/slice)
links = []
url = 'http://books.toscrape.com/index.html'
response = requests.get(url)
if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	categories = soup.find('ul')
	for categorie in categories:
		ctg = categories.findAll('a')['href'].replace('..','http://books.toscrape.com/catalogue/category/books')
		links.append(ctg)
"""

#Pour récupérer l'ensemble des livres d'une catégorie (terminé)
links =[]
bookData = {}
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
def get_book_urls(url):
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.text, 'lxml')
		articles = soup.findAll('article')
		for article in articles:
			a = article.find('a')['href'].replace('../../..','http://books.toscrape.com/catalogue')
			links.append(a)
			next = soup.find('li', {'class': 'next'})	
			if next:
				link = next.find('a')['href']
				suite = url.replace('index.html',link)
				links.append(get_book_urls(suite))
get_book_urls(url)

#Pour récuperer toutes les informations d'un livre (terminé)
def get_book_data(links):
	response = requests.get(links)
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

#Pour écrire les informations du livre (problème d'organisation dans le csv + Key error 'upc' ligne 59)
file = open('bookData.csv', 'w+')
file.write('product_page_url, universal_ product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url, \n')
for info in links:
	file.write(str(links)+','+str(bookData['upc'])+','+bookData['title']+','+str(bookData['price_including_tax'])+','+str(bookData['price_excluding_tax'])+','+str(bookData['number_available'])+','+bookData['product_description']+','+bookData['category']+','+bookData['review_rating']+','+str(bookData['image_url']+"\n"))
	file.close()

#Pour télécharger la première couverture du livre (comment creer les fichiers dans le dossier pictureData)
os.mkdir('pictureData')
for photo in bookData['image_url']:
	picture = requests.get(bookData['image_url'])
	image =open(bookData['title']+'.png', "wb")
	image.write(picture.content)
	picture.close()

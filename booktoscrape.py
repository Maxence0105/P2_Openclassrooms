import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/index.html'

#Pour récupérer l'ensemble des catégories:
def get_categories(url):
	ctgLinks = []
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.text, 'html.parser')
		menu = soup.find('ul', {'class': 'nav nav-list'})
		categories = menu.findAll('a')
		for categorie in categories:
			ctg = 'http://books.toscrape.com/' + categorie['href']
			ctgLinks.append(ctg)
	return ctgLinks[1:]

#Pour récupérer l'ensemble des livres d'une catégorie :
def get_book_urls(url):
	bookLinks = []
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.text, 'lxml')
		articles = soup.findAll('article')
		for article in articles:
			a = article.find('a')['href'].replace('../../..','http://books.toscrape.com/catalogue')
			bookLinks.append(a)
#Pour changer de page :
	next = soup.find('li', {'class': 'next'})	
	if next:
		page = next.find('a')['href']
		suite = url.split('/')
		suite[-1] = page
		bookLinks += get_book_urls('/'.join(suite))
	return bookLinks

#Pour récuperer toutes les informations d'un livre:
def get_book_data(url):
	bookData = {}
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.content, 'lxml')
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

try:
	os.mkdir('pictureData')
except:
	pass

try:
	os.mkdir('Data')
except:
	pass

ctgLinks = get_categories(url)
for url in ctgLinks:
	b = url.replace('http://books.toscrape.com/catalogue/category/books/','').replace('/index.html','')
	file = open('Data/'+ b +'.csv', 'w+', encoding="utf-8")
	file.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url,\n')		
	bookLinks = get_book_urls(url)
	for book_url in bookLinks:
		bookData = get_book_data(book_url)
		file.write(
			book_url+','+str(bookData['upc'])+','+bookData['title'].replace(',','').replace(';','').replace('\n','')+
			','+str(bookData['price_including_tax'])+','+str(bookData['price_excluding_tax'])+
			','+str(bookData['number_available'])+','+bookData['product_description'].replace('\n','').replace(',','').replace(';','').replace('"','')+
			','+bookData['category'].replace('\n','')+','+bookData['review_rating'].replace('\n','').replace(',','').replace(';','')+','+str(bookData['image_url']+"\n")
		)
		picture = requests.get(bookData['image_url'])
		image =open('pictureData/' + bookData['title'].replace(':','').replace('/',' ').replace('"','').replace('*','.').replace('?','')+'.png', "wb")
		image.write(picture.content)
	picture.close()
	file.close()	

print('l\'extraction de donnée s\'est déroulé avec succès !')
import requests

#число hh вакансий по опредлённому слову
def numb_in_hh(word):
	url = 'https://hh.ru/search/vacancy?text='+word+'&area=113&page=0'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
						 'AppleWebKit/537.36 (KHTML, like Gecko) '
						 'Chrome/79.0.3945.117 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
						 'Connection': 'keep-alive'}
	try:
		stat = requests.get(url, headers=headers) #запрос на сайт
		number=stat.text.split("></div><h1")[1].split("</h1></div>")[0].split(">")[1].split("вак")[0].replace("\xa0","") #Выделение числа из всего текста
		return int(number)
	except:
		return 0

#число the New York Times употребление опред слова
def numb_in_tnyt(word):
	url = 'https://www.nytimes.com/search?query='+word
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
						 'AppleWebKit/537.36 (KHTML, like Gecko) '
						 'Chrome/79.0.3945.117 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
						 'Connection': 'keep-alive'}
	try:
		stat = requests.get(url, headers=headers) #запрос на сайт
		number=stat.text.split("Showing")[1].split("results")[0].replace(" ","").replace(",","")  #Выделение числа из всего текста
		return int(number)
	except:
		return 0

#тестовые запросы
def main() :

	print("Число вакансий на hh.ru по слову python:",numb_in_hh("python"))
	print("Число упоминаний на nytimes.com слова python:",numb_in_tnyt("python"))



#если файл исполняемый, то запуск функции main
if __name__ == '__main__': 
	main()


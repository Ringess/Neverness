#!/data/data/com.termux/files/usr/bin/python3
from bs4 import BeautifulSoup
import requests

def get_html(url): #получает html-код страницы
    r=requests.get(url)
    return r.text

def get_data(html): #парсит данные со страницы
    parse=BeautifulSoup(html, 'lxml')
    get.text=parse.find('div',id='content').find('header', 'entry-header').text
    return get.text

def main(): #Вызывает функции в нужном порядке
    url='https://pythonworld.ru/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()




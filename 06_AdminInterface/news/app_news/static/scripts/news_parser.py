import requests
from bs4 import BeautifulSoup

def get_links_from_main(url):
    # список для ссылок на новости
    news_link_list = []

    # заголовок для обхода защиты на сайте
    headers = {'accept': '*/*', 
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

    # запрос html кода сайта
    request = requests.get(url, headers=headers)

    # парсинг html кода
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # список див-блоков с осноными новостями
    news = soup.find('div', {'class':'feed__chunk'})

    # выбираем каждый новостной блок и достаем оттуда ссылку
    for n in news.find_all('div', {'class':'feed__item'}):
        news_link_list.append(n.find('a', {'class':'content-feed__link'})['href'])

    return news_link_list

def get_content_from_news_pages(news_link_list):
    headers_list = []
    content_blocks = []
    
    # Проходимся по всем ссылкам
    for link in news_link_list:
        # заголовок для обхода защиты на сайте
        headers = {'accept': '*/*', 
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

        # запрос html кода сайта
        request = requests.get(link, headers=headers)

        # парсинг html кода
        soup = BeautifulSoup(request.text, 'html.parser')
        
        # парсинг заголовка
        headers_list.append(soup.find('h1', {'class':'content-title'}).get_text(strip=True))
        
        # парсинг основного текста
        content = soup.find('div', {'class':'content--full'})

        content_elements = []
        for elem in content.find_all('div', {'class':'l-island-a'}):
            content_elements.append(elem.get_text(strip=True))

        content_elements.pop(1) # удаляем справочный элемент с кол-вом просмотров
        content_blocks.append(' '.join(content_elements))

    return headers_list, content_blocks
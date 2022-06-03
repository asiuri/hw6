import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/'
HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
             "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64"
              "Safari/537.36 Edg/101.0.1210.53"
}



def get_html(url, params=" "):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []
    for item in items:
        films.append({
            'time': item.find("td").getText(),
            'div': item.find("h2", class_="b-content__inline_item-cover").getText(),
            'about': item.find("b-post__description_text ").getText(),
            'link': "https://rezka.ag/" + item.get('href'),
            "image": "https://rezka.ag/" + item.find('div', class_='b-content__columns pdt clearfix').find('img id').get('src').get('style')
        })
    return films


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for page in range(1, 2):
            html = get_html(f"{URL}page1_{page}.php")
            films.extend(get_data(html.text))
        # print(films)
        return films
    else:
        raise Exception("ERROR in parser!")


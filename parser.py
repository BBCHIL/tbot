import requests
from bs4 import BeautifulSoup


def money_rate():
    """
    Возвращает строку, в которой хранится нынешний курс доллара.
    """
    url = 'https://www.akchabar.kg'
    HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 13982.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.162 Safari/537.36"}

    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')

    rate_list = soup.find('ul', {'class': 'list-inline'})
    all_rates = (rate_list.find_all('li'))
    
    result = []
    for rate in all_rates:
        rate = ' '.join(rate.stripped_strings)
        result.append(rate)
    
    return '\n'.join(result)


def weather():
    """
    Возвращает строку, с расписанием погоды на неделю.
    """
    url = 'https://world-weather.ru/pogoda/kyrgyzstan/bishkek/'
    HEADERS = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 13982.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.162 Safari/537.36"}

    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, 'lxml')

    weather_list = soup.find('ul', {'id': 'vertical_tabs'})
    result = []
    for weather in weather_list:
        info = ' '.join(weather.stripped_strings)
        result.append(info)
    return '\n'.join(result)


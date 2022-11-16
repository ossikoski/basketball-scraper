import requests
import datetime

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.__prices_url = 'https://www.liigamanageri.net/hinnat'

        self.__reference_request = requests.get(self.__prices_url)
        self.__soup = BeautifulSoup(self.__reference_request.text, features='html.parser')

        self.__basket_url = 'https://basket.fi/basket/sarjat/pelaajatilastot/?league_id=4&season_id=125119'
        self.__basket_request = requests.get(self.__basket_url)
        self.__basket_soup = BeautifulSoup(self.__basket_request, features='html.parser')
        print(self.__basket_soup)

    def prices(self):
        price_data = {}
        for tbody in self.__soup.find_all('tbody'):
            for tr in tbody.find_all('tr'):
                for i, td in enumerate(tr.find_all('td')):
                    td = td.get_text()
                    if i == 0:
                        name = td
                        price_data[name] = []
                    if i == 3:
                        price_data[name] = td

        return price_data

def main():
    s = Scraper()
    price_data = s.prices()

if __name__ == '__main__':
    main()

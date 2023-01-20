import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.__prices_url = 'https://www.liigamanageri.net/hinnat'
        self.__reference_request = requests.get(self.__prices_url)
        self.__soup = BeautifulSoup(self.__reference_request.text, features='html.parser')

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.__browser = webdriver.Chrome('C:/Users/Ossi/Downloads/chromedriver_win32/chromedriver.exe', options=options)
        self.__browser.implicitly_wait(30)
        self.__browser.get('https://basket.fi/basket/sarjat/pelaajatilastot/?league_id=4&season_id=125119')

    def get_prices(self):
        """
        Get prices of players in liigamanageri
        """
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

    def stats(self):
        """
        Get stats of players
        Stats include games, points, assists, rebounds, offensive rebounds, blocks, 3pm, efficiency
        Nested for loop go brrrr
        """
        categories = ['Pisteet', 'Syötöt', 'Levypallot', 'Hyökkäyslevypallot', 'Torjunnat', 'Onnistuneet 3P heitot', 'Tehokkuus']
        stats = {}
        for category_i, category in enumerate(categories):
            self.__selector(category=category)
            for page_index in range(1, 8):
                if page_index != 1:
                    self.__change_page(page=page_index)
                table = self.__browser.find_element(by=By.ID, value='mbt-v2-player-stats-averages-table')
                rows = table.find_elements(by=By.TAG_NAME, value='tr')
                for row in rows:
                    cells = row.find_elements(by=By.TAG_NAME, value='td')
                    if cells and cells[0].text != '':
                        if cells[1].text not in stats.keys():
                            stats[cells[1].text] = []
                            stats[cells[1].text].append(cells[3].text)
                            if category_i > 0:  # Add zeros for other stats
                                stats[cells[1].text].extend([0]*category_i)
                            stats[cells[1].text].append(cells[5].text)
                        else:
                            stats[cells[1].text].append(cells[5].text)

        return stats

    def __selector(self, category):
        """
        Select which category in stats to browse
        """
        selector = self.__browser.find_element(by=By.ID, value='2-600-filter-stats')
        buttons = selector.find_elements(by=By.TAG_NAME, value='option')
        for b in buttons:
            if b.text == category:
                b.click()

    def __change_page(self, page):
        """
        Change to desired page
        """
        page_id = f'2-600-page-{page}'
        page_button = self.__browser.find_element(by=By.ID, value=page_id)
        page_button.click()

    def __del__(self):
        self.__browser.quit()


def main():
    s = Scraper()
    price_data = s.get_prices()
    stats = s.stats()
    print(stats)

if __name__ == '__main__':
    main()

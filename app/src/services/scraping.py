import requests
from bs4 import BeautifulSoup
from app.src.controller.game_data import GameData


class Scraping(GameData):
    def __init__(self):
        GameData.__init__(self)
        self.web = requests.get("https://www.nuuvem.com/promo/nintendo?utm_source=Nintendo&utm_medium=landing_page")
        print("Collecting promotions {}".format("https://www.nuuvem.com/promo"))

    def get_games_collection(self):
        try:
            self.__get_attribute_game()
        except:
            print("shocked climb :(")
            self.ad_data_order(0, 1, 'Game Mock', 'R$ 01,00', 'https://mock', 'https://mock.jpg')

    def __get_attribute_game(self):
        self.web_page = BeautifulSoup(self.web.text, "html.parser")
        products_list = self.web_page.find('div', {'class',
                                                   'products-dock--main nvm-mod mod-group-sell mod-group-sell-offer'}).find_all(
            'div', {'class', 'product-card--grid'})
        for p in products_list:
            util = p.find('div', {'class',
                                  'product__available product__purchasable product-card product-card__cover product-btn-add-to-cart--container'})

            self.add_game_database(products_list.index(p),
                                   1,
                                   util.get('data-track-product-name'),
                                   util.get('data-track-product-price'),
                                   util.get('data-track-product-url'),
                                   util.get('data-track-product-image-url'),
                                   )

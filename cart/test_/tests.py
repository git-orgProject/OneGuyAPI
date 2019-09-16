import json
from unittest import TestCase
import random
import requests


test_data = {

}


class ShopCartTest(TestCase):
    def test_all_users(self):
        url = 'http://127.0.0.1:8000/api/cart/?format=json'
        resp = requests.get(url)
        user_list = resp.json()
        print(user_list)

    def test_all_carts(self):
        url = 'http://127.0.0.1:8000/api/CommodityCart/?format=json'
        resp = requests.get(url)
        cart_list = resp.json()
        print(cart_list)


if __name__ == '__main__':
    ShopCartTest()

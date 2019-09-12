from unittest import TestCase
import requests


class CommodityTestCase(TestCase):

    def test_commodity(self):
        url = 'http://localhost:8000/goods/commodity/'
        resp = requests.get(url)
        commodity_list = resp.json().get('data')
        print(commodity_list)

    def test_commoditypk(self):
        url = 'http://localhost:8000/goods/commoditypk'
        resp = requests.get(url,params={'id':'0513e390-1d4d-4a85-8f67-b499a6e7b943'})
        commodity_list = resp.json().get('data')
        print(commodity_list)

    def test_commodityfk(self):
        url = 'http://localhost:8000/goods/commodityfk'
        resp = requests.get(url,params={'id':'34c19d99-19a6-4e86-9144-18a8670cc577'})
        commodity_list = resp.json().get('data')
        print(commodity_list)




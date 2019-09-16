import requests
import unittest
from unittest import TestCase, TestSuite, TextTestRunner





class UserTestCase(TestCase):
    def test_01_category(self):
        url = 'http://localhost:8000/goods/f_category'
        resp = requests.get(url)
        category_list = resp.json().get('data')
        print(category_list)



    def test_02_category(self):
        url = 'http://localhost:8000/goods/s_category/ad7f227d-73c0-44a2-9edd-924006deb134'
        resp = requests.get(url)

        category_list1 = resp.json().get('data')
        print(category_list1)
    def test_03_category(self):
        url = 'http://localhost:8000/goods/category_list'
        resp = requests.get(url)

        category_list = resp.json().get('data')
        print(category_list)

    def test_03_coupon(self):
        url = 'http://localhost:8000/goods/coupon/4'
        resp = requests.get(url)

        category_list = resp.json().get('data')
        print(category_list)

if __name__ == '__main__':
    unittest.main()

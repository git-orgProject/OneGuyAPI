import random
import unittest
from unittest import TestCase
import requests

test_data = {

}

class CityTestCase(TestCase):


    def test_01_city(self):
        url = 'http://localhost:8000/active/city'
        resp = requests.get(url)
        cha = random.choice(list(map(chr, range(ord('A'), ord('Z') + 1))))
        city_list = resp.json().get('data')[cha]
        city = random.choice(city_list)
        test_data['city_id'] = city['id']
        print('--当前城市--%s'%  city['cityName'])





    def test_02_city_area(self):
        url = 'http://localhost:8000/active/area'

        resp = requests.get(url,{
            'id':'9a2b361285294ddf86bd60b7a46444a7'
        })
        area_list = resp.json().get('data')
        area = random.choice(area_list)
        print('--当前区县--%s'% area['AreaName'] )
        # self.area_id = area['id']
        test_data['area_id'] = area['id']
        print(test_data['area_id'])

    def test_03_commodity(self):
        url = 'http://localhost:8000/active/area/commod'
        print(test_data['area_id'])
        resp = requests.get(url, {
            'id': test_data['area_id']
        })
        commod_list = resp.json().get('data')
        for i  in commod_list:
            print(i['commodity']['commodityName'])


    def test_04_active(self):
        url = 'http://localhost:8000/active/act'
        resp = requests.get(url)
        act_list = resp.json().get('data')
        for act in act_list:
            print(act)

    def test_05_active(self):
        url = 'http://localhost:8000/active/nav'
        resp = requests.get(url)
        nav_list = resp.json().get('data')
        for nav in nav_list:
            print(nav)


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     suitel = unittest.TestSuite()
#     suitel.addTest(CityTestCase.test_dll_city)
#
#     suite2 = unittest.TestSuite()
#     suitel.addTest(CityTestCase.test_css_city)
#
#     all_suite = unittest.TestSuite((suitel,suite2))
#
#     unittest.TextTestRunner().run(all_suite)
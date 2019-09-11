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
        city_list = resp.json().get('data')
        city = random.choice(city_list)
        test_data['city_id'] = city['id']
        print('--当前城市--'% city.cityName)





    def test_02_city_area(self):
        url = 'http://localhost'
        resp = requests.get(url,{
            'one_id':test_data['city_id']
        })
        area_list = resp.json().get('data')
        area = random.choice(area_list)
        print()
        self.area_id = area['id']

# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    suitel = unittest.TestSuite()
    suitel.addTest(CityTestCase.test_dll_city)

    suite2 = unittest.TestSuite()
    suitel.addTest(CityTestCase.test_css_city)

    all_suite = unittest.TestSuite((suitel,suite2))

    unittest.TextTestRunner().run(all_suite)
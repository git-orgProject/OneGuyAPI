from django.test import TestCase

import requests
import unittest
from unittest import TestCase, TestSuite, TextTestRunner
import random


test_data = {

}

class addCartTestCase(TestCase):

    def test_user(self):
        url = 'http://localhost:8000/api/cart/'
        resp = requests.post(url)
        user_list = resp.json()
        # user = random.choice(user_list)
        print('---定位当前的用户---', user_list, type(user_list))

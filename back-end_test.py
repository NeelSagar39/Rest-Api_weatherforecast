import requests
import unittest

base_url = 'http://3.82.248.105/'


class InterfacesTest:
    def __init__(self):
        self.interfaces_test_urls = {
            'temp_predictions': 'get-temp-predictions',
            'rainfall_predictions': 'get-rainfall-predictions',
            'humidity_predictions': 'get-humidity-predictions',
            'wind_predictions': 'get-wind-predictions',
            'cloudy_predictions': 'get-cloudy-predictions',
            'weekly_temperature': 'get-temp-weekly',
        }

    def test(self):
        # record the status after iterative tests
        pass


class UnitTest(unittest.TestCase):

    @staticmethod
    def test():
        pass


interface_test = InterfacesTest()
unit_test = UnitTest()

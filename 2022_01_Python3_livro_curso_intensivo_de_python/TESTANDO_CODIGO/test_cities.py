# arquivo que chama o modulo city_functions

from city_functions import city_country
import unittest

class TestCityFunc(unittest.TestCase):
    def test_city_country(self):
        formatado = city_country('Osasco', 'São Paulo', 10)
        self.assertEqual(formatado, 'osasco são paulo 10')

unittest.main()
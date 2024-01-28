# TESTANDO O MODULO NAME FUNCTION 

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function.py'."""
    def test_first_last_name(self):
        """Nomes como 'Janis joplin' funcionam?"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    

unittest.main()
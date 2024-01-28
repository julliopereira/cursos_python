import unittest
from name_function_middle_name import get_formatted_name

class NamesTestCase(unittest.TestCase):                         # chamar unittes.TestCase para relizar os tests
    """Testes para 'name_function.py'."""
    def test_first_last_name(self):                             # cria um modulo para tratar primeiro e ultimo nome
        """Nomes como 'Janis joplin' funcionam?"""
        formatted_name = get_formatted_name('Janis','Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):                      # cria segundo modulo para tratar nome sobrenome e ultimo nome
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnounymousSurvey"""
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        print(my_survey.responses)

unittest.main()

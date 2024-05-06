import unittest
from credit_score_handler import CreditScoreHandler
from data_loader import load_data

class TestCreditScoreHandler(unittest.TestCase):
    def setUp(self):
        data = load_data('data/Car_Insurance_Claim.csv')
        self.credit_score_handler = CreditScoreHandler(data)

    def test_credit_score_calculation(self):
        params = {
            'idade': 30,
            'sexo': 'male',
            'anos_experiencia': 15,
            'escolaridade': 'university',
            'renda': 'working class',
            'ano_veiculo': 'before 2015',
            'tipo_veiculo': 'sedan',
            'quilometragem_anual': 10000
        }
        expected_credit_score = 0.4375620702636496
        credit_score = self.credit_score_handler.calculate_credit_score(params)
        self.assertEqual(credit_score, expected_credit_score)

    def test_no_data_found(self):
        params = {
            'idade': 18,
            'sexo': 'female',
            'anos_experiencia': 5,
            'escolaridade': 'high school',
            'renda': 'poverty',
            'ano_veiculo': 'after 2015',
            'tipo_veiculo': 'suv',
            'quilometragem_anual': 15000
        }
        credit_score = self.credit_score_handler.calculate_credit_score(params)
        self.assertIsNone(credit_score)

if __name__ == '__main__':
    unittest.main()

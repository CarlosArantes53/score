import unittest
from app import app

class TestCreditScoreEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_credit_score_endpoint(self):   # Testando uma solicitação bem-sucedida
        response = self.app.post('/credit-score', query_string={
            'idade': 30,
            'sexo': 'male',
            'anos_experiencia': 5,
            'escolaridade': 'university',
            'renda': 'middle class',
            'ano_veiculo': 'after 2015',
            'tipo_veiculo': 'sedan',
            'quilometragem_anual': 10000
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('CREDIT_SCORE', data)

    def test_invalid_request(self):   # Testando uma solicitação inválida
        response = self.app.post('/credit-score', query_string={
            'idade': 20,
            'sexo': 'male',
            'anos_experiencia': 1,
            'escolaridade': 'none',
            'renda': 'poverty',
            'ano_veiculo': 'before 2015',
            'tipo_veiculo': 'sports car',
            'quilometragem_anual': 5000
        })
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Não foi possível encontrar dados correspondentes aos critérios fornecidos')

if __name__ == '__main__':
    unittest.main()

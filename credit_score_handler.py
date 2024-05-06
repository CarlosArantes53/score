import pandas as pd

class CreditScoreHandler:
    def __init__(self, data):
        self.data = data

    def categorize_age(self, age):
        if age < 25:
            return '16-25'
        elif age < 40:
            return '26-39'
        elif age < 65:
            return '40-64'
        else:
            return '65+'

    def categorize_experience(self, experience):
        if experience < 10:
            return '0-9y'
        elif experience < 20:
            return '10-19y'
        elif experience < 30:
            return '20-29y'
        else:
            return '30y+'

    def calculate_credit_score(self, params):
        idade = self.categorize_age(params['idade'])
        anos_experiencia = self.categorize_experience(params['anos_experiencia'])
        sexo = params['sexo']
        escolaridade = params['escolaridade']
        renda = params['renda']
        ano_veiculo = params['ano_veiculo']
        tipo_veiculo = params['tipo_veiculo']
        quilometragem_anual = params['quilometragem_anual']

        filtered_data = self.data[
            (self.data['AGE'] == idade) &
            (self.data['GENDER'] == sexo) &
            (self.data['DRIVING_EXPERIENCE'] == anos_experiencia) &
            (self.data['EDUCATION'] == escolaridade) &
            (self.data['INCOME'] == renda) &
            (self.data['VEHICLE_YEAR'] == ano_veiculo) &
            (self.data['VEHICLE_TYPE'] == tipo_veiculo)
        ]

        if filtered_data.empty:
            return None

        credit_score = filtered_data['CREDIT_SCORE'].mean()
        return credit_score

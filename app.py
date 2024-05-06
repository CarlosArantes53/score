from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from #OpenAPI
from config import Config
from credit_score_handler import CreditScoreHandler
from data_loader import load_data

app = Flask(__name__)
app.config.from_object(Config)
swagger = Swagger(app)

data = load_data('data/Car_Insurance_Claim.csv')
credit_score_handler = CreditScoreHandler(data)

@app.route('/credit-score', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'idade',
            'in': 'query',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'sexo',
            'in': 'query',
            'type': 'string',
            'enum': ['male', 'female'],
            'required': True
        },
        {
            'name': 'anos_experiencia',
            'in': 'query',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'escolaridade',
            'in': 'query',
            'type': 'string',
            'enum': ['high school', 'university', 'none'],
            'required': True
        },
        {
            'name': 'renda',
            'in': 'query',
            'type': 'string',
            'enum': ['poverty', 'working class', 'upper class', 'middle class'],
            'required': True
        },
        {
            'name': 'ano_veiculo',
            'in': 'query',
            'type': 'string',
            'enum': ['before 2015', 'after 2015'],
            'required': True
        },
        {
            'name': 'tipo_veiculo',
            'in': 'query',
            'type': 'string',
            'enum': ['sedan', 'sports car'],
            'required': True
        },
        {
            'name': 'quilometragem_anual',
            'in': 'query',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Score de crédito calculado com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'CREDIT_SCORE': {'type': 'number'}
                        }
                    }
                }
            }
        },
        '404': {
            'description': 'Não foi possível encontrar dados correspondentes aos critérios fornecidos',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'message': {'type': 'string'}
                        }
                    }
                }
            }
        }
    }
})
def get_credit_score():
    params = {
        'idade': int(request.args.get('idade')),
        'sexo': request.args.get('sexo'),
        'anos_experiencia': int(request.args.get('anos_experiencia')),
        'escolaridade': request.args.get('escolaridade'),
        'renda': request.args.get('renda'),
        'ano_veiculo': request.args.get('ano_veiculo'),
        'tipo_veiculo': request.args.get('tipo_veiculo'),
        'quilometragem_anual': int(request.args.get('quilometragem_anual'))
    }

    credit_score = credit_score_handler.calculate_credit_score(params)
    if credit_score is None:
        return jsonify({'message': 'Não foi possível encontrar dados correspondentes aos critérios fornecidos'}), 404

    return jsonify({'CREDIT_SCORE': credit_score})

if __name__ == '__main__':
    app.run()

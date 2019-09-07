"""
API  for  fetching capital using country name

"""
from flask import Flask, jsonify
app = Flask(__name__)  # pylint: disable=invalid-name

DATA_FILE_PATH = 'data/Country_Capital.txt'


def get_capital_via_country_name(country_name):
    """
    This function return the capital name from
    'Country_Capital.txt' using country

    """
    with open(DATA_FILE_PATH, mode='r') as countries_capitals:

        for country_capital in countries_capitals.readlines():
            if country_name == country_capital.split(',')[0].rstrip():
                # store capital of a country
                capital = country_capital.split(',')[1].rstrip()
                return capital

        return -1


@app.route('/getcapital/<string:country_name>', methods=['GET'])
def get_capital(country_name):
    """
    Implementation of HTTP GET Method

    """
    response = get_capital_response(country_name)

    return jsonify(response)


def get_capital_response(country_name):
    """
     Get capital of a country

    """
    capital = get_capital_via_country_name(country_name)

    # pylint: disable=line-too-long

    response = generate_error_response() if capital == -1 else generate_success_response(country_name, capital)  # nopep8

    return response


def generate_success_response(country, capital):
    """
    return capital of country

    """
    response = {'country': country, 'capital': capital}

    return response


def generate_error_response():
    """
    return error message

    """
    response = {'message': "Country doesn't exist"}

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

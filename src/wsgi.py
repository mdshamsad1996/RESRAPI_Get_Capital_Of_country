"""
Gunicorn WSGI HTTP server
"""
from get_capital_of_country import app as application

if __name__ == '__main__':
    application.run()

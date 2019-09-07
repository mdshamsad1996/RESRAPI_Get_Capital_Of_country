"""
Unit test case of get_capital_of_country API

"""
import unittest
from src.get_capital_of_country import get_capital_via_country_name, \
     get_capital_response


class TestingGetCapitalOfCountry(unittest.TestCase):
    """
    Test class of get_capital_of_country API
    """
    def test_get_capital_for_proper_country(self):
        """
        Test case of proper country for get_capital_via_country_name() function

        """
        capital_expected_1 = 'New Delhi'
        capital_received_1 = get_capital_via_country_name('India')

        capital_expected_2 = 'Luanda'
        capital_received_2 = get_capital_via_country_name('Angola')

        self.assertEqual(capital_expected_1, capital_received_1)
        self.assertEqual(capital_expected_2, capital_received_2)

    def test_get_capital_for_improper_country(self):
        """
         Test case of improper country for
         get_capital_via_country_name() function

        """
        error_expected = -1
        error_received = get_capital_via_country_name('Bangalore')
        self.assertEqual(error_expected, error_received)

    def test_get_capital_response_for_proper_country(self):
        """
         Test case of proper country for get_capital_response() function

        """
        capital_expected = {'country': 'India', 'capital': 'New Delhi'}
        capital_received = get_capital_response('India')

        self.assertEqual(capital_expected, capital_received)

    def test_get_capital_response_for_improper_country(self):
        """
         Test case of improper country for get_capital_response() function

        """
        message_expected = {'message': "Country doesn't exist"}
        message_received = get_capital_response('Kolkata')
        self.assertEqual(message_expected, message_received)


if __name__ == '__main___':
    unittest.main()

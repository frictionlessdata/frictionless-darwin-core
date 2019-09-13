import unittest
from FrictionlessDarwinCore import DwCVocabulary


class TestVocabulary(unittest.TestCase):

    def test_load(self):
        """
        Test that it can load DwC vocabulary from a csv file
        """
        v = DwCVocabulary()
        self.assertIsNotNone(v)
        self.assertEqual(v.size(), 232)

    def test_case_insensitiveness(self):
        """
        Test that it can retrieve 'countrycode', 'COUNTRYCODE' or 'CountryCode'
        """
        v = DwCVocabulary()

        country_code1 = v.term('http://rs.tdwg.org/dwc/terms/countrycode')
        self.assertIsNotNone(country_code1)
        country_code2 = v.term('http://rs.tdwg.org/dwc/terms/COUNTRYCODE')
        self.assertIsNotNone(country_code2)
        country_code3 = v.term('http://rs.tdwg.org/dwc/terms/CountryCode')
        self.assertIsNotNone(country_code3)

    def test_term(self):
        """
        Test that it can retrieve 'basisOfRecord' and 'countryCode'(valid DwC terms) but not 'Zorglub'(a fictional one)
        """
        v = DwCVocabulary()
        basis_of_record = v.term('http://rs.tdwg.org/dwc/terms/basisOfRecord')
        self.assertIsNotNone(basis_of_record)

        country_code = v.term('http://rs.tdwg.org/dwc/terms/countryCode')
        self.assertIsNotNone(country_code)
        self.assertTrue('class' in country_code)
        self.assertTrue('type' in country_code)
        self.assertTrue('format' in country_code)
        self.assertTrue('constraints' in country_code)
        self.assertTrue('comment' in country_code)

        event_date = v.term('http://rs.tdwg.org/dwc/terms/eventDate')
        self.assertEqual(event_date['type'],'string')

        zorglub = v.term('http://rs.tdwg.org/dwc/terms/Zorglub')
        self.assertIsNone(zorglub)


if __name__ == '__main__':
    unittest.main()

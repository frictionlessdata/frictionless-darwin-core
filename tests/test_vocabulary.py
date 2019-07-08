import unittest

from FrictionlessDarwinCore import DwCVocabulary

class TestVocabulary(unittest.TestCase):
    path= '../data/fdwc_terms.csv'

    def test_load(self):
        """
        Test that it can load DwC vocabulary from a csv file
        """
        dwcVoc = DwCVocabulary(TestVocabulary.path)
        self.assertIsNotNone(dwcVoc)
        self.assertEqual(dwcVoc.size(), 123)

    def test_case_insensitiveness(self):
        """
        Test that it can retrieve 'countrycode', 'COUNTRYCODE' or 'CountryCode'
        """
        dwcVoc = DwCVocabulary(TestVocabulary.path)

        countryCode1 = dwcVoc.term('countrycode')
        self.assertIsNotNone(countryCode1)
        countryCode2 = dwcVoc.term('COUNTRYCODE')
        self.assertIsNotNone(countryCode2)
        countryCode3 = dwcVoc.term('CountryCode')
        self.assertIsNotNone(countryCode3)

    def test_term(self):
        """
        Test that it can retrieve 'basisOfRecord' and 'countryCode'(valid DwC terms) but not 'Zorglub'(a fictional one)
        """
        dwcVoc = DwCVocabulary(TestVocabulary.path)
        basisOfRecord = dwcVoc.term('basisOfRecord')
        self.assertIsNotNone(basisOfRecord)

        countryCode = dwcVoc.term('countryCode')
        self.assertIsNotNone(countryCode)
        self.assertTrue('class' in countryCode)
        self.assertTrue('type' in countryCode)
        self.assertTrue('format' in countryCode)
        self.assertTrue('constraints' in countryCode)
        self.assertTrue('comment' in countryCode)

        zorglub = dwcVoc.term('Zorglub')
        self.assertIsNone(zorglub)


if __name__ == '__main__':
    unittest.main()

import unittest

from FrictionlessDarwinCore import DwCMetadata

class TestMetadata(unittest.TestCase):
    S0path = 'data/S0eml.xml'
    S0url = 'http://ipt.ala.org.au/eml.do?r=global'
    S0hd= 'f85862dab043121553ffe6875a92cb0a'

    def test_SOurl(self):
        """
        Test that SOurl can be retrieve and documented with correct secure hash
        """
        m = DwCMetadata(TestMetadata.S0url)
        self.assertIsNotNone(m)
        hd= m.document()
        self.assertEqual(hd,TestMetadata.S0hd)

    def test_SOpath(self):
        """
        Test that SOpath can be opened and documented with correct secure hash
        """
        m = DwCMetadata(TestMetadata.S0path)
        self.assertIsNotNone(m)
        hd= m.document()
        self.assertEqual(hd,TestMetadata.S0hd)

if __name__ == '__main__':
    unittest.main()

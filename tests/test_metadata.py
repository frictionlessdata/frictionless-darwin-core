import unittest
from FrictionlessDarwinCore import DwCMetadata


class TestMetadata(unittest.TestCase):
    S0eml = '../data/S0/eml.xml'
    S0hd = '43c8372f9e965afd09a0b464191de924'
    C1eml = '../data/C1/eml.xml'
    C1hd = '4fc7f7a6a666d7b143471285ff49c27b'
    T1eml = '../data/T1/eml.xml'
    T1hd = 'af947a7d455fc8f4c1cab163d901de2a'
    T2eml = '../data/T2/eml.xml'
    T2hd = 'cde8ddfd707796872e78ddb042055b05'
    T3eml = '../data/T3/eml.xml'
    T3hd = 'd6588189021d784c6916241e388d549a'

    def test_C1eml(self):
        """
        Test that COeml can be opened and documented with expected secure hash and content
        """
        f = open(TestMetadata.C1eml)
        m = DwCMetadata(f.read())
        f.close()
        self.assertIsNotNone(m)
        m.convert()
        self.assertTrue(m.valid)
        self.assertEqual(m.hexdigest, TestMetadata.C1hd)

    def test_SOeml(self):
        """
        Test that SOeml can be opened and documented with expected secure hash and content
        """
        f = open(TestMetadata.S0eml)
        m = DwCMetadata(f.read())
        f.close()
        self.assertIsNotNone(m)
        m.convert()
        self.assertTrue(m.valid)
        self.assertEqual(m.hexdigest, TestMetadata.S0hd)

    def test_T3eml(self):
        """
        Test that T3eml can be opened and documented with expected secure hash and content
        """
        f = open(TestMetadata.T3eml)
        eml = f.read()
        f.close()
        m = DwCMetadata(eml)
        self.assertIsNotNone(m)
        m.convert()
        self.assertTrue(m.valid)
        self.assertEqual(m.hexdigest, TestMetadata.T3hd)

if __name__ == '__main__':
    unittest.main()

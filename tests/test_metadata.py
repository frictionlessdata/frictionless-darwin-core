import unittest
from FrictionlessDarwinCore import DwCMetadata


class TestMetadata(unittest.TestCase):
    S0eml = '../data/S0/eml.xml'
    S0hd = '3e95b95a887b3fb7b5019b6daa4dfd2b'
    C1eml = '../data/C1/eml.xml'
    C1hd = '7c15bff57d4b6f3811865b3ff5743792'
    T1eml = '../data/T1/eml.xml'
    T1hd = 'af947a7d455fc8f4c1cab163d901de2a'

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

    def test_T1eml(self):
        """
        Test that T1eml can be opened and documented with expected secure hash and content
        """
        f = open(TestMetadata.T1eml)
        eml = f.read()
        f.close()
        m = DwCMetadata(eml)
        self.assertIsNotNone(m)
        m.convert()
        self.assertTrue(m.valid)
        self.assertEqual(m.hexdigest, TestMetadata.T1hd)

if __name__ == '__main__':
    unittest.main()

import unittest

from FrictionlessDarwinCore import DwCMetadata

class TestMetadata(unittest.TestCase):
    S0path = 'data/S0eml.xml'
    S0url = 'http://ipt.ala.org.au/eml.do?r=global'
    S0hd= '6864c0b0ffd6e257593cf7804b042848'

    def test_SO(self):
        """
        Test that SO can be documented
        """
        m = DwCMetadata(TestMetadata.S0url)
        self.assertIsNotNone(m)
        hd= m.document()
        self.assertEqual(hd,TestMetadata.S0hd)

if __name__ == '__main__':
    unittest.main()

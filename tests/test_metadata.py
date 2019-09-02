import unittest

from FrictionlessDarwinCore import DwCMetadata

class TestMetadata(unittest.TestCase):
    S0eml = '../data/S0/eml.xml'
    S0readme = '../data/S0/readme.md'
    S0url = 'http://ipt.ala.org.au/eml.do?r=global'
    S0hd= '35fd4823b18f3520828fcfe957381455'


    def test_SOeml(self):
        """
        Test that SOeml can be opened and documented with expected secure hash and content
        """
        f=open(TestMetadata.S0eml)
        m = DwCMetadata(f.read())
        f.close()
        self.assertIsNotNone(m)
        m.convert()
        self.assertEqual(m.hexdigest,TestMetadata.S0hd)

if __name__ == '__main__':
    unittest.main()

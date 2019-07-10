import unittest

from FrictionlessDarwinCore import DwCPackage

class TestPackage(unittest.TestCase):
    url_S1 = 'https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles'
    pathS1 = 'data/dwca_S1.zip'

    def test_infer(self):
        """
        Test that it can infer a Package from path
        """
        p = DwCPackage(TestPackage.pathS1)
        self.assertIsNotNone(p)
        p.infer()
        self.assertTrue(p.valid)

if __name__ == '__main__':
    unittest.main()

import unittest

from FrictionlessDarwinCore import DwCArchive

class TestArchive(unittest.TestCase):
    S1url = 'https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37'


    def test_load(self):
        """
        Test that S1url can be loaded
        """
        dwca=DwCArchive(TestArchive.S1url)
        self.assertIsNotNone(dwca)
        self.assertTrue(dwca.valid)

    def test_infer(self):
        """
        Test that S1url can be infered
        """
        dwca=DwCArchive(TestArchive.S1url)
        self.assertIsNotNone(dwca)
        dwca.infer()
        self.assertTrue(dwca.valid)

if __name__ == '__main__':
    unittest.main()

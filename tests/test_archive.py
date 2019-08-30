import unittest

from FrictionlessDarwinCore import DwCArchive

class TestArchive(unittest.TestCase):
    S1url = 'https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37'


    def test_S1(self):
        """
        Test DarwinCore Archive can be loaded, inferred and saved from S1url
        """
        dwca=DwCArchive(TestArchive.S1url)
        self.assertIsNotNone(dwca)
        self.assertTrue(dwca.valid)
        dwca.infer()
        self.assertTrue(dwca.valid)
        dwca.save()
        self.assertTrue(dwca.valid)


if __name__ == '__main__':
    unittest.main()

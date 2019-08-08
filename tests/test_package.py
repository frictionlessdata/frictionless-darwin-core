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

    def test_eventDate(self):
        """
        Test that 'event' field is there with 'string' type and 'default' format
        """
        p = DwCPackage(TestPackage.pathS1)
        self.assertIsNotNone(p)
        p.infer()
        self.assertTrue(p.valid)
        r=p.get_resource('occurrence')
        self.assertIsNotNone(r)
        eventDate_field = r.schema.get_field('eventDate')
        self.assertIsNotNone(eventDate_field)
        self.assertEqual(eventDate_field.type, 'string')
        self.assertEqual(eventDate_field.format, 'default')


if __name__ == '__main__':
    unittest.main()

import unittest

from FrictionlessDarwinCore import DwCResource

class TestResource(unittest.TestCase):
    path = 'data/occurrence.txt'

    def test_infer(self):
        """
        Test that it can infer a Resource from a txt file
        """
        r = DwCResource({'path': TestResource.path})
        self.assertIsNotNone(r)
        r.infer()
        self.assertTrue(r.schema.valid)

    def test_fields(self):
        """
        Test that it can retrieve fields
        """
        r = DwCResource({'path': TestResource.path})
        self.assertIsNotNone(r)
        r.infer()
        self.assertIsNotNone(r.schema.get_field('countryCode'))
        self.assertIsNotNone(r.schema.get_field('basisOfRecord'))
        self.assertIsNotNone(r.schema.get_field('decimalLatitude'))
        self.assertIsNotNone(r.schema.get_field('decimalLongitude'))
        self.assertIsNone(r.schema.get_field('zorglub'))

    def test_id(self):
        """
        Test that 'id' field is there
        """
        r = DwCResource({'path': TestResource.path})
        self.assertIsNotNone(r)
        r.infer()
        id_field=r.schema.get_field('id')
        self.assertIsNotNone(id_field)

if __name__ == '__main__':
    unittest.main()

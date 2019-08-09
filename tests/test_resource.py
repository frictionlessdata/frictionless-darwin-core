import unittest

from FrictionlessDarwinCore import DwCResource

class TestResource(unittest.TestCase):
    path = 'data/occurrence.csv'

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
        r = DwCResource({'path': TestResource.path}, '../tests/')
        self.assertIsNotNone(r)
        r.infer()
        self.assertIsNotNone(r.schema.get_field('countryCode'))
        self.assertIsNotNone(r.schema.get_field('basisOfRecord'))
        self.assertIsNotNone(r.schema.get_field('decimalLatitude'))
        self.assertIsNotNone(r.schema.get_field('decimalLongitude'))
        self.assertIsNone(r.schema.get_field('zorglub'))

    def test_eventDate(self):
        """
        Test that 'event' field is there with 'string' type and 'default' format
        """
        r = DwCResource({'path': TestResource.path}, '../tests/')
        self.assertIsNotNone(r)
        r.infer()
        eventDate_field=r.schema.get_field('eventDate')
        self.assertIsNotNone(eventDate_field)
        self.assertEqual(eventDate_field.type,'string')
        self.assertEqual(eventDate_field.format,'default')

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

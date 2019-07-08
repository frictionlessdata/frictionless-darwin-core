import unittest

from FrictionlessDarwinCore import DwCTable

class TestTable(unittest.TestCase):
    path = '../data/occurrence.txt'

    def test_load(self):
        """
        Test that it can load Table from a csv file
        """
        table = DwCTable(TestTable.path)
        self.assertIsNotNone(table)
        table.infer()
        self.assertTrue(table.schema.valid)

    def test_fields(self):
        """
        Test that it can retrieve Table fields
        """
        table = DwCTable(TestTable.path)
        self.assertIsNotNone(table)
        table.infer()
        self.assertIsNotNone(table.schema.get_field('countryCode'))
        self.assertIsNotNone(table.schema.get_field('basisOfRecord'))
        self.assertIsNotNone(table.schema.get_field('decimalLatitude'))
        self.assertIsNotNone(table.schema.get_field('decimalLongitude'))
        self.assertIsNone(table.schema.get_field('zorglub'))

    def test_id(self):
        """
        Test that 'id' field is there
        """
        table = DwCTable(TestTable.path)
        self.assertIsNotNone(table)
        table.infer()
        id_field=table.schema.get_field('id')
        self.assertIsNotNone(id_field)

if __name__ == '__main__':
    unittest.main()

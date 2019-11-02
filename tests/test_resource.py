import unittest
from hashlib import blake2b
from FrictionlessDarwinCore import DwCResource
import xml.etree.ElementTree as ET


class TestResource(unittest.TestCase):

    D1meta = '../data/D1/meta.xml'
    D1data = '../data/D1/classification.txt'
    D1hd = '57bb9a0319d4b4386dc7f1da011fb339'
    ns = {'dwc': 'http://rs.tdwg.org/dwc/text/'}


    def test_D1(self):
        """
        Test that D1 data and meta can be opened and data file can be generated with appropriate content
        """
        m = open(TestResource.D1meta)
        d = open(TestResource.D1data)
        archive = ET.fromstring(m.read())
        core = archive.find('dwc:core', TestResource.ns)
        r = DwCResource(core, d.read())
        m.close()
        d.close()
        self.assertIsNotNone(r)
        h = blake2b(key=b'FrictionlessDarwinCore', digest_size=16)
        data = r.convert()
        h.update(data.encode('UTF-8'))
        self.assertTrue(r.valid)
        self.assertEqual(h.hexdigest(), TestResource.D1hd)
        print(data)

if __name__ == '__main__':
    unittest.main()

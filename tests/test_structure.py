import unittest
from hashlib import blake2b
from FrictionlessDarwinCore import DwCStructure


class TestStructure(unittest.TestCase):
    S1json = '../data/S1/datapackage.json'
    S1eml = '../data/S1/eml.xml'
    S1meta = '../data/S1/meta.xml'
    S1url = 'http://ipt.ala.org.au/eml.do?r=global'
    S1hd = '55a798c68cefaaaded739b6bee4c3fd9'
    T3eml = '../data/T3/eml.xml'
    T3meta = '../data/T3/meta.xml'
    T3hd = 'fdc639bdbe91add7be894212df38c1dd'

    def test_SO(self):
        """
        Test that S1 eml and meta can be opened and datapackage can be generated with appropriate content
        """
        e = open(TestStructure.S1eml)
        m = open(TestStructure.S1meta)
        s = DwCStructure(m.read(), e.read())
        m.close()
        e.close()
        self.assertIsNotNone(s)
        h = blake2b(key=b'FrictionlessDarwinCore', digest_size=16)
        h.update(s.convert().encode('UTF-8'))
        self.assertEqual(h.hexdigest(), TestStructure.S1hd)

    def test_T3(self):
        """
        Test that T3 eml and meta can be opened and datapackage can be generated with appropriate content
        """
        e = open(TestStructure.T3eml)
        m = open(TestStructure.T3meta)
        s = DwCStructure(m.read(), e.read())
        m.close()
        e.close()
        self.assertIsNotNone(s)
        h = blake2b(key=b'FrictionlessDarwinCore', digest_size=16)
        h.update(s.convert().encode('UTF-8'))
        self.assertEqual(h.hexdigest(), TestStructure.T3hd)

if __name__ == '__main__':
    unittest.main()

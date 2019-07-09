from datapackage import Resource
from FrictionlessDarwinCore import DwCVocabulary
from pathlib import Path
import zipfile

class DwCResource(Resource):
    voc = DwCVocabulary('../data/fdwc_terms.csv')

    def __init__(self, descriptor):
        Resource.__init__(self, descriptor)
        self.descriptor['format'] = 'csv'
        self.commit()

    def infer(self):
        Resource.infer(self)
        for field in self.schema.fields:
            term = self.voc.term(field.name)
            if term:
                self.schema.update_field(field.name, {'type': term['type']})
                self.schema.update_field(field.name, {'format': term['format']})
        self.schema.commit()

if __name__ == '__main__':
    dataPath = Path('data/occurrence.txt')
    r = DwCResource({'path': str(dataPath)})
    r.infer()
    r.save('../tmp/dataresource.json')
    print(r.descriptor)

from datapackage import Resource
from FrictionlessDarwinCore import DwCVocabulary
from pathlib import Path
import zipfile

class DwCResource(Resource):
    voc = DwCVocabulary()

    def __init__(self, descriptor,base_path=None):
        Resource.__init__(self, descriptor,base_path=base_path)
        self.descriptor['format'] = 'csv'
        self.commit()

    def infer(self):
        Resource.infer(self)
        for field in self.schema.fields:
            term = self.voc.term(field.name)
            if term:
                self.schema.update_field(field.name, {'type': term['type']})
                self.schema.update_field(field.name, {'format': term['format']})
            else:
                print(field.name)
        self.schema.commit()

if __name__ == '__main__':
    dataPath = Path('data/Occurrence.txt')
    r = DwCResource({'path': str(dataPath)}, '../tests/')
    r.infer()
    print(r.descriptor)

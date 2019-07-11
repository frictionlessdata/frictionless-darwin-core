from datapackage import Resource
from FrictionlessDarwinCore import DwCVocabulary
from pathlib import Path
import zipfile

class DwCResource(Resource):
    voc = DwCVocabulary()

    def __init__(self, descriptor,base_path=None):
        Resource.__init__(self, descriptor,base_path=base_path)

    def infer(self):
        Resource.infer(self)
        if self.descriptor['format'] == 'csv': # a DarwinCore data file
            for field in self.schema.fields:
                term = self.voc.term(field.name)
                if term:
                    self.schema.update_field(field.name, {'type': term['type']})
                    self.schema.update_field(field.name, {'format': term['format']})
                else:
                    if field.name != 'id': # not a DawrinCore term
                        print('Not a DarwinCore term:',field.name)
        else:
            print('Not a csv format:', self.descriptor)


if __name__ == '__main__':
    dataPath = Path('data/Occurrence.csv')
    r = DwCResource({'path': str(dataPath)}, '../tests/')
    r.infer()
    print(r.schema.descriptor)

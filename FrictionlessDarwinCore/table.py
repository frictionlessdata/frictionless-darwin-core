from tableschema import Table
from FrictionlessDarwinCore import DwCVocabulary

class DwCTable(Table):
    voc = DwCVocabulary('../data/fdwc_terms.csv')

    def __init__(self, file):
        Table.__init__(self, file, format='csv')

    def infer(self):
        Table.infer(self)
        for field in self.schema.fields:
            term = self.voc.term(field.name)
            if term:
                self.schema.update_field(field.name, {'type': term['type']})
                self.schema.update_field(field.name, {'format': term['format']})
        self.schema.commit()

if __name__ == '__main__':
    table = DwCTable('../data/occurrence.txt')
    table.infer()
    table.save('../tmp/t1/data.csv')
    table.schema.save('../tmp/t1/dataschema.json')
    print(table.schema.descriptor)

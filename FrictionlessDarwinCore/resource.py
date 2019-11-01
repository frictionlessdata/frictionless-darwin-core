from FrictionlessDarwinCore import DwCVocabulary
import xml.etree.ElementTree as ET
import csv
import io

class DwCResource:
    voc = DwCVocabulary()
    ns = {'dwc': 'http://rs.tdwg.org/dwc/text/'}

    def __init__(self, meta, data):
        self.meta = meta
        self.data = data
        self.valid = True
        self.rows= []

    def convert(self):
        self.rows= []
        fields={}
        if self.meta is not None:
            mfile = ET.fromstring(self.meta)
        for f in mfile.findall('field'):
            if f.get('default') is None:
                fields[f.get('term')] = ''
            else:
                fields[f.get('term')] = f.get('default')
        datareader = csv.reader(self.data.split('\n'), delimiter='\t')
        header = []
        for f in fields:
            header.append(f.rsplit('/', 1)[1])
        self._append(header)
        skip = True
        for inrow in datareader:
            if skip or len(inrow) == 0:
                skip = False
            else:
                outrow=[]
                index=0
                for fname, fvalue in fields.items():
                    if fvalue == '':
                        outrow.append(inrow[index])
                        index=index+1
                    else:
                        outrow.append(fvalue)
                self._append(outrow)
        self.valid = True
        return self.as_csv()

    def as_csv(self):
        output = io.StringIO()
        datawriter = csv.writer(output, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for r in self.rows:
            datawriter.writerow(r)
        return output.getvalue()

    def _append(self, row):
        self.rows.append(row)


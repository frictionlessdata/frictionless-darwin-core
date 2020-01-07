from FrictionlessDarwinCore import DwCVocabulary
import xml.etree.ElementTree as ET
import csv
import io

class DwCResource:
    voc = DwCVocabulary()
    ns = {'dwc': 'http://rs.tdwg.org/dwc/text/'}

    def __init__(self, meta: ET, data: str):
        self.meta = meta
        self.data = data.decode('utf-8')
        self.core = meta.tag.endswith('core')
        self.valid = True
        self.rows= []

    def _get_fields(self):
        fields={}
        if self.meta is None:
            return
        index_id='0'

        if self.core:
            index = self.meta.find('dwc:id', DwCResource.ns)
        else:
            index = self.meta.find('dwc:coreid', DwCResource.ns)
        if index is not None:
            index_id = index.get('index')

        need_additional_id_field = True
        for f in self.meta.findall('dwc:field', DwCResource.ns):
            if f.get('index') == index_id:
                need_additional_id_field = False

        if need_additional_id_field:
            fields['http://rs.tdwg.org/dwc/text/id'] = ''

        for f in self.meta.findall('dwc:field', DwCResource.ns):
            if f.get('default') is None:
                fields[f.get('term')] = ''
            else:
                fields[f.get('term')] = f.get('default')
        return fields

    def convert(self):
        if self.meta is None:
            return
        self.rows= []
#        print(ET.tostring(self.meta))
        fields = self._get_fields()
        datareader = csv.reader(self.data.split(self._delimiter('linesTerminatedBy')),
            delimiter=self._delimiter('fieldsTerminatedBy'))
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
        quotechar=self._delimiter('fieldsEnclosedBy')
        if quotechar == '':
            quoting = csv.QUOTE_NONE
        else:
            quoting = csv.QUOTE_MINIMAL
        datawriter = csv.writer(output, lineterminator= self._delimiter('linesTerminatedBy'),
                                delimiter = self._delimiter('fieldsTerminatedBy'),
                                quotechar=quotechar,
                                quoting=quoting)
        for r in self.rows:
            datawriter.writerow(r)
        return output.getvalue()

    def _delimiter(self, delimiter_string):
        switcher = {
            "\\n": '\n',
            "\\r": '\r',
            "\\r\\n": '\r\n',
            "\\t": '\t',
        }
        ds = self.meta.get(delimiter_string)
        if ds is not None:
            return switcher.get(ds, ds)
        else:
            if delimiter_string == 'fieldsEnclosedBy':
                return '"'
            else:
                return ''

    def _append(self, row):
        self.rows.append(row)


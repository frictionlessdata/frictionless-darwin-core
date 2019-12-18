from FrictionlessDarwinCore import DwCVocabulary
import xml.etree.ElementTree as ET
import re
import json


class DwCStructure:
    voc = DwCVocabulary()
    ns = {'dwc': 'http://rs.tdwg.org/dwc/text/'}

    def __init__(self, meta, eml, meta_dir =''):
        self.eml = eml
        self.meta = meta
        self.meta_dir = meta_dir
        self.descriptor = {}
        self.corename = ''
        self.pkey_name = 'id'
        self.has_default_values = False
        self.valid = True

    def convert(self):
        # convert meta.xml into datapackage descriptor
        try:
            self.descriptor = {}
            if self.eml is not None:
                dataset = ET.fromstring(self.eml).find('./dataset')
                self._addheader(dataset)
            if self.meta is not None:
                archive = ET.fromstring(self.meta)
                resources = []
                core = archive.find('dwc:core', DwCStructure.ns)
                self.corename = core.get('rowType').rsplit('/', 1)[1].lower()

                resources.append(self._toresource(core, True))
                for extension in archive.findall('dwc:extension', DwCStructure.ns):
                    resources.append(self._toresource(extension, False))
                self._add('resources', resources)
        except BaseException as err:
            self.valid = False
            print(err, 'in DwCStructure.convert()')
        else:
            self.valid = True
        return self.as_json()

    def as_json(self):
        return json.dumps(self.descriptor)


    def _add(self, key, value):
        self.descriptor[key] = value

    def _addheader(self, dataset):
        licences = []
        sources = []
        for ai in dataset.findall('./alternateIdentifier'):
            m = re.search(r'(?<==)\w+', ai.text)
            if m is not None:
                self._add('name', m.group(0))
            if re.search('^[0-9a-f\-]*$', ai.text):
                self._add('id', ai.text)
            if re.search('^https?://', ai.text):
                source = {'title': 'GBIF IPT', 'path': ai.text}
                sources.append(source)
        title=dataset.find('.title')
        if title is not None:
            self._add('title', title.text)
        self._add('profile', 'tabular-data-package')
        ipr = dataset.find('./intellectualRights')
        if ipr is not None:
            licence = {}
            ulink = ipr.find('./para/ulink')
            if ulink is not None:
                ct = ulink.findtext('./citetitle')
                if ct is not None:
                    name = re.search('\((.+)\)', ct)
                    if name is not None:
                        licence['name'] = name.group(0)
                    licence['title'] = ct
                licence['path'] = ulink.get('url')
            licences.append(licence)
        self._add('licences', licences)

        self._add('sources', sources)

    def _delimiter(self, delimiter_string):
        switcher = {
            "\\n": '\n',
            "\\r": '\r',
            "\\r\\n": '\r\n',
            "\\t": '\t',
        }
        if delimiter_string is not None:
            return switcher.get(delimiter_string, delimiter_string)
        else:
            return ''

    def _toresource(self, mfile, core):
        if mfile is None:
            return
        r = {}
        files = mfile.find('dwc:files', DwCStructure.ns)
        location = files.find('dwc:location', DwCStructure.ns)
        r['name'] = location.text.split('.')[0].lower()
        r['path'] = location.text
        r['rdfType'] = mfile.get('rowType')
        r['profile'] = 'tabular-data-resource'
        r['encoding'] = mfile.get('encoding')
        r['format'] = 'csv'
        dialect = {'csvddfVersion': 1.2, 'delimiter': self._delimiter(mfile.get('fieldsTerminatedBy')),
                   'doubleQuote': True, 'lineTerminator': self._delimiter(mfile.get('linesTerminatedBy')),
                   'quoteChar': self._delimiter(mfile.get('fieldsEnclosedBy')), 'skipInitialSpace': True,
                   'header': mfile.get('ignoreHeaderLines') == '1', 'commentChar': '#'}
        r['dialect'] = dialect

        schema = {}
        fields = []

        index_id='0'
        index_name = 'id'

        if core:
            index = mfile.find('dwc:id', DwCStructure.ns)
        else:
            index = mfile.find('dwc:coreid', DwCStructure.ns)
        if index is not None:
            index_id = index.get('index')

        need_additional_id_field = True
        for f in mfile.findall('dwc:field', DwCStructure.ns):
            if f.get('index') == index_id:
                need_additional_id_field = False
                index_name = f.get('term').rsplit('/', 1)[1]
                if core:
                    self.pkey_name = index_name

        if need_additional_id_field:
            print('Adding additional_id_field')
            field = {'name': index_name, 'type': 'string', 'format': 'default'}
            fields.append(field)

        for f in mfile.findall('dwc:field', DwCStructure.ns):
            field = {}
            mterm = f.get('term')
            term = self.voc.term(mterm)
            if term is None:
                print(mterm, 'unknown Darwin Core term.')
                field['name'] = mterm.rsplit('/', 1)[1]
                field['type'] = 'string'
            else:
                field['name'] = term['name']
                field['type'] = term['type']
                field['rdfType'] = mterm
                if term['format'] != 'default':
                    field['format'] = term['format']
                if term['constraints'] != '':
                    field['constraints'] = json.loads(term['constraints'])
            if f.get('default') is not None:
                self.has_default_values = True
            fields.append(field)
        schema['fields'] = fields
        r['schema'] = schema
        if core:
            r['primaryKey'] = self.pkey_name
        else:
            fkeys = []
            fkey = {}

            fkey['fields'] = index_name
            ref = {}
            ref['resource'] = self.corename
            ref['fields'] = self.pkey_name
            fkey['reference'] = ref
            fkeys.append(fkey)
            r['foreignKeys'] = fkeys
        return r

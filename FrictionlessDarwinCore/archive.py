from FrictionlessDarwinCore import *
from pathlib import Path

import sys
import shutil
import requests
import zipfile
import tempfile
import xml.etree.ElementTree as ET


class DwCArchive:
    voc = DwCVocabulary()
    ns = {'dwc': 'http://rs.tdwg.org/dwc/text/'}

    def __init__(self, path_or_url):
        self.valid = True
        self.dwca = path_or_url
        self.meta_dir = ''
        self.metadata = None
        self.structure = None
        self.tf = None
        self.need_conversion = False
        if self.dwca.startswith('http'):
            self.path = self.download()
        else:
            self.path = self.dwca

    def download(self):
        #  download DwCArchive into temporary file
        self.tf = tempfile.NamedTemporaryFile()
        try:
            response = requests.get(self.dwca)
            self.tf.write(response.content)
        except requests.exceptions.RequestException as err:
            print(err)
            self.valid = False
        else:
            print('downloading ' + self.dwca + ' as ' + self.tf.name)
        return self.tf.name

    def infer(self):
        if zipfile.is_zipfile(self.path):
            self.load()
        else:
            self.valid = False
            print('dwca is not a zipfile')

    def load(self):
        eml = ''
        meta = ''
        zf = zipfile.ZipFile(self.path, mode='r')
        try:
            for info in zf.infolist():
                p=Path(info.filename)
                if p.name in ('eml.xml','metadata.xml'):
                    eml = zf.read(info.filename).decode()
                if p.name == 'meta.xml':
                    meta = zf.read(info.filename).decode()
                    self.meta_dir = p.parent.name
            if eml != '' and meta != '':
                self.metadata = DwCMetadata(eml)
                self.structure = DwCStructure(meta, eml, self.meta_dir)
                self.metadata.convert()
                self.structure.convert()
                self.valid = self.metadata.valid and self.structure.valid
                self.need_conversion = self.structure.has_default_values
            else:
                print('EML or Meta file missing')
                self.valid = False
        except BaseException:
            print(sys.exc_info())
            print('load zip failed')
            self.valid = False
        finally:
            zf.close()

    def _load_data(self, zf, filename, meta):
        try:
            resource = None
            for info in zf.infolist():
                p = Path(info.filename)
                if p.name == filename:
                    data = zf.read(info.filename).decode()
                    resource = DwCResource(meta, data)
        except KeyError:
            print ('Did not find %s in zip file' % p)
            self.valid = False
        except BaseException:
            print(sys.exc_info())
            print('load data from zip failed')
            self.valid = False
        return resource

    def save(self, output):
        if self.need_conversion:
            # convert all data files
            self._save_data(output)
            self._save_dwc_meta(output)
        else:
            # No Data conversion need, first copy zipfile to output
            shutil.copyfile(self.path, output)
        self._save_meta(output)

    def _save_meta(self, output):
        # Append structure and metadata
        zf = zipfile.ZipFile(output, mode='a')
        try:
             # Add a README.md file that describes the package
            zf.writestr('readme.md', self.metadata.as_markdown())
            # Add a datapackage.json
            zf.writestr('datapackage.json', self.structure.as_json())
        except IOError as e:
            print("Unable to copy file. %s" % e)
        else:
            print('saving zipfile to ' + output)
        finally:
            zf.close()

    def _save_dwc_meta(self, output):
        # Append original eml.xml , meta.xml or metadata.xml in meta_dir
        izf = zipfile.ZipFile(self.path, mode='r')
        ozf = zipfile.ZipFile(output, mode='a')
        try:
            for info in izf.infolist():
                p=Path(info.filename)
                if p.parent.name == self.meta_dir and p.suffix == '.xml' and not p.name.startswith('.'):
                    print ('copying ',info.filename, self.meta_dir)
                    ozf.writestr(p.name, izf.read(info.filename).decode())
        except BaseException:
            print(sys.exc_info())
            print('load zip failed')
            self.valid = False
        finally:
            izf.close()
            ozf.close()

    def _save_data(self, output):
        # create empty output zipfile
        izf = zipfile.ZipFile(self.path, mode='r')
        ozf = zipfile.ZipFile(output, mode='w')
        # add core and extension data as CSV files
        try:
            archive = ET.fromstring(self.structure.meta)
            core = archive.find('dwc:core', DwCArchive.ns)
            files = core.find('dwc:files', DwCArchive.ns)
            location = files.find('dwc:location', DwCArchive.ns)
            resource = self._load_data(izf, location.text, core)
            if resource is not None:
                ozf.writestr(location.text, resource.convert())
            for extension in archive.findall('dwc:extension', DwCArchive.ns):
                files = extension.find('dwc:files', DwCArchive.ns)
                location = files.find('dwc:location', DwCArchive.ns)
                resource = self._load_data(izf,location.text, extension)
                if resource is not None:
                    ozf.writestr(location.text, resource.convert())
        except IOError as e:
            print("Unable to copy file. %s" % e)
        finally:
            izf.close()
            ozf.close()

    def to_csv(self, output):
        self._save_data(output)

    def to_json(self, output):
        o = open(output, 'w')
        try:
            o.write(self.structure.as_json())
        except IOError as e:
            print("Unable to write file. %s" % e)
        else:
            print('saving json to ' + output)
        finally:
            o.close()

    def to_markdown(self, output):
        o = open(output, 'w')
        try:
            o.write(self.metadata.as_markdown())
        except IOError as e:
            print("Unable to write file. %s" % e)
        else:
            print('saving markdown to ' + output)
        finally:
            o.close()

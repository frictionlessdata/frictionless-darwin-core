from FrictionlessDarwinCore import *
from pathlib import Path

import sys
import shutil
import requests
import zipfile
import tempfile



class DwCArchive:
    voc = DwCVocabulary()

    def __init__(self, path_or_url):
        self.valid = True
        self.dwca = path_or_url
        self.metadata = None
        self.structure = None
        self.tf = None
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
        meta_dir = ''
        zf = zipfile.ZipFile(self.path, mode='r')
        try:
            for info in zf.infolist():
                p=Path(info.filename)
                if p.name in ('eml.xml','metadata.xml'):
                    eml = zf.read(info.filename).decode()
                if p.name == 'meta.xml':
                    meta = zf.read(info.filename).decode()
                    meta_dir = p.parent.name
            if eml != '' and meta != '':
                self.metadata = DwCMetadata(eml)
                self.structure = DwCStructure(meta, eml, meta_dir)
                self.metadata.convert()
                self.structure.convert()
                self.valid = self.metadata.valid and self.structure.valid
            else:
                print('EML or Meta file missing')
                self.valid = False
        except BaseException:
            print(sys.exc_info())
            print('load zip failed')
            self.valid = False
        finally:
            zf.close()

    def save(self, output):
        # first copy zipfile to output
        shutil.copyfile(self.path, output)
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

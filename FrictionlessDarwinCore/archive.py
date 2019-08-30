from pathlib import Path
from FrictionlessDarwinCore import *

import requests
import io
import zipfile

class DwCArchive:
    voc = DwCVocabulary()

    def __init__(self, dwca_pathOrUrl):
        self.dwca=dwca_pathOrUrl
        if self.dwca.startswith('http'):
            self.download()
        else:
            self.zippath = self.dwca
        self.load()

    def infer(self):
        self.metadata.convert()
        self.structure.convert()
        self.valid = self.metadata.valid and self.structure.valid

    def save(self):
        try:
            zf = zipfile.ZipFile(self.zippath, mode='a')
            # Add a README.md file that describes the package
            zf.writestr('readme.md', self.metadata.as_markdown())
            # Add a datapackage.json
            zf.writestr('datapackage.json', self.structure.as_json())
        except:
            print('writing to zipfile failed')
        finally:
            zf.close()

    def download(self):
        #  download DwCArchive
        try:
            self.zippath = Path('../tmp/fdwc.zip')
            response = requests.get(self.dwca)
            f=open(self.zippath, 'wb')
            f.write(response.content)
            f.close()
        except:
            print('download failed')
            self.valid=False;
        finally:
            f.close()

    def load(self):
        try:
            zf = zipfile.ZipFile(self.zippath, mode='r')
            for info in zf.infolist():
                if info.filename=='eml.xml':
                    eml=zf.read(info.filename).decode()
                if info.filename=='metadata.xml':
                    eml=zf.read(info.filename).decode()
                if info.filename=='meta.xml':
                    meta=zf.read(info.filename).decode()
            self.metadata = DwCMetadata(eml)
            self.structure = DwCStructure(meta, eml)
            self.valid=eml !='' and meta !=''
        except:
            print('load zip failed')
            self.valid=False;
        finally:
            zf.close()

    def to_json(self, o):
        try:
            o.write(self.structure.as_json())
        except:
            print('writing to_json failed')
        finally:
            o.close()

    def to_markdown(self, o):
        try:
            o.write(self.metadata.as_markdown())
        except:
            print('writing to_markdown failed')
        finally:
            o.close()

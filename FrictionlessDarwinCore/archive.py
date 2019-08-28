from pathlib import Path
from FrictionlessDarwinCore import *

import requests
import io
import zipfile

class DwCArchive:
    voc = DwCVocabulary()

    def __init__(self, dwca_pathOrUrl):
        self.dwca=dwca_pathOrUrl
        self.eml = ''
        self.meta = ''
        self.load()

    def infer(self):
        self.metadata = DwCMetadata(self.eml)
        self.metadata.convert()
        self.structure = DwCStructure(self.meta,self.eml)
        self.structure.convert()
        self.valid = self.metadata.valid and self.structure.valid


    def save(self):
        try:
            zf = zipfile.ZipFile(self.zippath, mode='a')
            # Add a README.md file that describes the package
            zf.writestr('readme.md', self.metadata.as_markdown())
            # Add a datapackage.json
            zf.writestr('datapackage.json', self.structure.as_json())
        finally:
            zf.close()

    def load(self):
        # infer structure from zip content
        try:
            if self.dwca.startswith('http'):
                # download it
                self.zippath = Path('../tmp/fdwc.zip')
                response = requests.get(self.dwca)
                f=open(self.zippath, 'wb')
                f.write(response.content)
                f.close()
            else:
               self.zippath= self.dwca

            zf = zipfile.ZipFile(self.zippath, mode='r')
            for info in zf.infolist():
                if info.filename=='eml.xml':
                    self.eml=zf.read(info.filename).decode()
                if info.filename=='metadata.xml':
                    self.eml=zf.read(info.filename).decode()
                if info.filename=='meta.xml':
                    self.meta=zf.read(info.filename).decode()
            self.valid=self.eml !='' and self.meta !=''

        finally:
            zf.close()

    def to_json(self, o):
        f= open (o, mode='w')
        f.write(self.structure.as_json())
        f.close

    def to_markdown(self, o):
        f= open (o, mode='w')
        f.write(self.metadata.as_markdown())
        f.close



if __name__ == '__main__':
#    dwca = DwCArchive('../tmp/dwca-rbins_saproxilyc_beetles-v9.37.zip')
    dwca = DwCArchive('https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37')
#    dwca= DwCArchive('https://ipt.biodiversity.be/archive.do?r=afromoths')
#    dwca= DwCArchive('https://ipt.biodiversity.be/archive.do?r=axiom')
#    dwca= DwCArchive('http://api.gbif.org/v1/occurrence/download/request/0004292-190813142620410.zip')
#    dwca= DwCArchive('http://apm-ipt.br.fgov.be:8080/ipt-2.3.5/archive.do?r=botanical_collection')
#    dwca=DwCArchive('../tmp/fdwc.zip')
    dwca.infer()


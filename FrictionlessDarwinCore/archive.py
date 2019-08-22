from pathlib import Path
from FrictionlessDarwinCore import *

import requests
import io
import zipfile

class DwCArchive:
    voc = DwCVocabulary()

    def __init__(self, dwca_pathOrUrl):
        self.dwca=dwca_pathOrUrl
        self.zippath = Path('../tmp/fdwc.zip')
        self.emlstring = ''
        self.metastring = ''

    def infer(self):
        # infer structure from zip content
        emlstring=''
        metastring=''
        if self.dwca.startswith('http'):
            # download it
            response = requests.get(self.dwca)
            f=open(self.zippath, 'wb')
            f.write(response.content)
            f.close()
        else:
            self.zippath= self.dwca
        try:
            zf = zipfile.ZipFile(self.zippath, mode='a')
            for info in zf.infolist():
                print(info.filename)
#            ofile = self.folder / info.filename
#            if ofile.suffix == '.txt':
#                ofile = ofile.with_suffix('.csv')
#            ofile.touch()
#            ofile.write_bytes(zf.read(info.filename))
#            self.datafiles.append(str(ofile))
                if info.filename=='eml.xml':
                    emlstring=zf.read(info.filename)
                if info.filename=='meta.xml':
                    metastring=zf.read(info.filename)

#                if info.filename.endswith('.txt'):
#                   zf.write(info.filename, arcname=info.filename.replace('.txt','.csv'))

            zf.writestr('readme.md', self.document(emlstring))
            zf.writestr('datapackage.json', self.structure(metastring,emlstring))
        finally:
            zf.close()

    def document(self, eml):
        # Add a README.md file that describes the package
        print('DwcArchive.Document()')
        metadata = DwCMetadata(eml)
        return metadata.convert()

    def structure(self,meta, eml):
        # Add a datapackage.json
        structure = DwCStructure(meta,eml)
        print('DwcArchive.Structure()')
        return structure.convert()


if __name__ == '__main__':
#    dwca = DwCArchive('../tmp/dwca-rbins_saproxilyc_beetles-v9.37.zip')
#    dwca = DwCArchive('https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37')
#    dwca= DwCArchive('https://ipt.biodiversity.be/archive.do?r=afromoths')
    dwca= DwCArchive('https://ipt.biodiversity.be/archive.do?r=axiom')
    dwca.infer()


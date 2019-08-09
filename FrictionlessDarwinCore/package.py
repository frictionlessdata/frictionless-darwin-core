from datapackage import Package, Resource
from tableschema import Field
from pathlib import Path
from FrictionlessDarwinCore import DwCVocabulary, DwCResource

import requests
import io
import zipfile
import datetime

class DwCPackage(Package):
    voc = DwCVocabulary()

    def __init__(self, dwca_pathOrUrl,base_path=None):
        Package.__init__(self,base_path=base_path)
        self.dwca=dwca_pathOrUrl

    def fromUrl(self):
        return dwca.startswith('http')

    def fromPath(self):
        return not dwca.startswith('http')

    def infer(self):
        if self.dwca.startswith('http'):
            response = requests.get(self.dwca)
            zf= zipfile.ZipFile(io.BytesIO(response.content))
        else:
            zf= zipfile.ZipFile(self.dwca)
#        fdp_folder = Path(self.dwca_path).parent / 'datapackage'
        fdp_folder = Path(self.base_path)
        fdp_folder.mkdir(0o777, False, True)
        Package.base_path=str(fdp_folder)
        for info in zf.infolist():
            ofile = fdp_folder / info.filename
            if ofile.suffix == '.txt':
                ofile = ofile.with_suffix('.csv')
            ofile.touch()
            ofile.write_bytes(zf.read(info.filename))
            r= DwCResource({'path': str(ofile.name)},base_path=self.base_path)
            r.infer()
            self.add_resource(r.descriptor)
        self.commit()

    def document(self):
        # Add a README.md file that describes the package
        ofile= Path(self.base_path) / 'README.md'
        text= 'Generated with FrictionlessDarwinCore on ' + str(datetime.datetime.now()) + '\nfrom DwCA: ' + self.dwca;
        ofile.write_text(text)

if __name__ == '__main__':
#    p = DwCPackage('../tmp/dwca-rbins_saproxilyc_beetles-v9.37.zip', '../tmp/datapackage')
    p = DwCPackage('https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37', '../tmp/datapackage')
    p.infer()
    p.document()
    p.save('../tmp/t1/my_first_fdwc.zip')
    print(p.valid)
    print(p.descriptor)

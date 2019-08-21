from datapackage import Package
from pathlib import Path
from FrictionlessDarwinCore import *

import requests
import io
import zipfile

class DwCPackage(Package):

    def __init__(self, description,base_path=None):
        Package.__init__(self,description,base_path=base_path)


    def infer(self):
    # infer data package from darwinCore archive
        if self.dwca.startswith('http'):
            response = requests.get(self.dwca)
            zf= zipfile.ZipFile(io.BytesIO(response.content))
        else:
            zf= zipfile.ZipFile(self.dwca)



if __name__ == '__main__':
#    p = DwCPackage('../tmp/dwca-rbins_saproxilyc_beetles-v9.37.zip', '../tmp/datapackage')
    p = DwCPackage('https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37', '../tmp/datapackage')
    p.infer()

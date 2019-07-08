from datapackage import Package, Resource
from pathlib import Path
import zipfile

class DwCPackage(Package):
    def __init__(self, dwca):
        self.dwca_path = Path(dwca)

    def infer(self):
        zf = zipfile.ZipFile(self.dwca_path)
        fdp_folder = self.dwca_path.parent / self.dwca_path.stem
        fdp_folder.mkdir(0o777, False, True)
        for info in zf.infolist():
            ofile = fdp_folder / info.filename
            if ofile.suffix == '.txt':
                ofile = ofile.with_suffix('.csv')
            ofile.touch()
            ofile.write_bytes(zf.read(info.filename))
            r= Resource({'path': ofile.as_posix()})
            r.infer()
            print(r.descriptor)
if __name__ == '__main__':
    p = DwCPackage('../tmp/dwca-rbins_saproxilyc_beetles-v9.37.zip')
    p.infer()

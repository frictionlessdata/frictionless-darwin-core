import argparse
from FrictionlessDarwinCore import DwCArchive

def cli():
    parser = argparse.ArgumentParser(description='DwCA to DataPackage converter')
    parser.add_argument('DwCA', help='path (or URL) to input DwC Archive')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o', dest='output', type=argparse.FileType('w'), help='path to datapackage, if not supplied DwCA will be updated')
    group.add_argument('-d', dest='descriptor', type=argparse.FileType('w'), help='path to descriptor(datapackage.json), DwCA untouched')
    parser.add_argument('-l', dest='loose', help='loose, no field constraints', action="store_true")
    args = parser.parse_args()
    dwca = DwCArchive(args['DwCA'])
    dwca.infer()

#parser.parse_args('https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles&v=9.37 -l -d ../tmp/dp.json'.split())

# Main program
if __name__ == '__main__':
    cli()

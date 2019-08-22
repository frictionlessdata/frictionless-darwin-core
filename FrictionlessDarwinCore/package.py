from datapackage import Package

class DwCPackage(Package):

    def __init__(self, path):
        Package.__init__(self,path)


if __name__ == '__main__':
#    p = Package(base_path='../tmp/fdwc/')
#    p.infer('occurrence.csv')
    p = Package('../tmp/fdwc.zip')
    print(p.valid)
    print(p.errors)

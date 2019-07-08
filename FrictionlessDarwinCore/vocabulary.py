import csv

class DwCVocabulary:

    def __init__(self,file):
        self.dwcTerms = dict()
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile, )
            for row in reader:
                termDict= dict()
                for x,y in row.items():
                    termDict[x]=y
                self.dwcTerms[row['name'].lower()]= termDict

    def term(self, name):
        if name.lower() in self.dwcTerms:
            return self.dwcTerms[name.lower()]

    def size(self):
            return len(self.dwcTerms)

if __name__ == '__main__':
    dwcVoc = DwCVocabulary('../data/fdwc_terms.csv')
    print(dwcVoc.term('countryCode'))


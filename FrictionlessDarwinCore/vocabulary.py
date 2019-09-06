import csv
import os

class DwCVocabulary:

    def __init__(self,path=None):
        self.dwcTerms = dict()
        if path==None:
            path = os.path.join(os.path.dirname(__file__), 'fdwc_terms.csv')
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                termDict= dict()
                for x,y in row.items():
                    termDict[x]=y
                self.dwcTerms[row['qualifiedName'].lower()]= termDict

    def term(self, name):
        if name.lower() in self.dwcTerms:
            return self.dwcTerms[name.lower()]


    def size(self):
            return len(self.dwcTerms)

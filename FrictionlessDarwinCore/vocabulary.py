import csv
import os


class DwCVocabulary:

    def __init__(self, path=None):
        self.dwc_dictionary = dict()
        if path is None:
            path = os.path.join(os.path.dirname(__file__), 'fdwc_terms.csv')
        with open(path, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                namespace = row['namespace'].lower()
                if namespace in self.dwc_dictionary:
                    ns = self.dwc_dictionary[namespace]
                else:
                    ns = dict()
                    self.dwc_dictionary[row['namespace'].lower()] = ns
                term = dict()
                for x, y in row.items():
                    term[x] = y
                ns[row['name'].lower()] = term

    def term(self, qualified_name):
        tokens = qualified_name.lower().rsplit("/", 1)
        if tokens[0] in self.dwc_dictionary:
            ns = self.dwc_dictionary[tokens[0]]
            if tokens[1] in ns:
                return ns[tokens[1]]
        return None

    def size(self):
        result = 0
        for k, ns in self.dwc_dictionary.items():
            result = result + len(ns)
        return result

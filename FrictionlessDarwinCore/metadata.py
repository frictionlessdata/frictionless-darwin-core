from pathlib import Path

import io
import datetime
import xml.etree.ElementTree as ET

class DwCMetadata:

    def __init__(self, emlfile):
        self.emlfile = emlfile
        self.allLines= []

    def document(self):
        self.allLines= []

        tree = ET.parse(self.emlfile)
        dataset=tree.getroot().find('./dataset')
        self._title(dataset.find('./title'))
        for ai in dataset.findall('./alternateIdentifier'):
            self._element(ai)
        self._element(dataset.find('./pubDate'))
        self._element(dataset.find('./language'))
        self._person(dataset.find('./creator'))
        self._person(dataset.find('./metadataProvider'))
        self._person(dataset.find('./associatedParty'))
        self._abstract(dataset.find('./abstract'))
        self._keywords(dataset)
        self._geographicCoverage(dataset.find('./coverage/geographicCoverage'))
        self._person(dataset.find('./contact'))
        self._add('# About')
        self._add('generated on '+ str(datetime.datetime.now()))
        self._add('with [FrictionlessDarwinCore](https://github.com/frictionlessdata/FrictionlessDarwinCore)')

    def save(self, toPath):
        ofile = open(toPath, "w")
        ofile.writelines(self.allLines)
        ofile.close()

    def _add(self, line):
        self.allLines.append(line + '\n\n')

    def _title(self, element):
        self._add('# ' + element.text)

    def _element(self, element):
        self._add(element.tag + ': '+ element.text)

    def _abstract(self, element):
        self._add('## Abstract')
        for p in element.findall('./para'):
            self._add(p.text)

    def _keywords(self, element):
        self._add('## Keywords')
        for k in element.findall('./keywordSet'):
            self._add('*'+ k.find('./keyword').text + '* ' + k.find('./keywordThesaurus').text)

    def _geographicCoverage(self, element):
        self._add('## Geographic Coverage')
        self._add('Description: ' + element.find('./geographicDescription').text)
        self._add('BoundingCoordinates: West:' + element.find('./boundingCoordinates/westBoundingCoordinate').text +
            '°, East:' + element.find('./boundingCoordinates/eastBoundingCoordinate').text +
            '°, North:' + element.find('./boundingCoordinates/northBoundingCoordinate').text +
            '°, South:' + element.find('./boundingCoordinates/southBoundingCoordinate').text + '°')


    def _person(self, element):
        self._add('## ' + element.tag)
        self._add('Name:'+element.find('./individualName/givenName').text + ' ' + element.find('./individualName/surName').text)
        self._add('Organization:'+element.find('./organizationName').text)
        self._add('email:'+element.find('./electronicMailAddress').text)


if __name__ == '__main__':
        m = DwCMetadata('../tests/eml.xml')
        m.document()
        m.save('../tmp/README.md')

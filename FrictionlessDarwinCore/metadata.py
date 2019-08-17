from pathlib import Path

import io
from hashlib import blake2b
import datetime
import requests
import xml.etree.ElementTree as ET

class DwCMetadata:

    def __init__(self, eml):
        self.eml = eml
        self.allLines= []

    def document(self):
        self.allLines= []
        if self.eml.startswith('http'):
            response = requests.get(self.eml)
            root= ET.fromstring(response.text)
        else:
            root = ET.parse(self.eml).getroot()
        dataset=root.find('./dataset')
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
        self._intellectualRigths(dataset)
        self._geographicCoverage(dataset.find('./coverage/geographicCoverage'))
        self._taxonomicCoverage(dataset.find('./coverage/taxonomicCoverage'))
        self._maintenance(dataset.find('./maintenance'))
        self._person(dataset.find('./contact'))
        self._methods(dataset.find('./methods'))
        self._project(dataset.find('./project'))
        self._additionalMetadata(root.find('./additionalMetadata'))
        hash =blake2b(key=b'FrictionlessDarwinCore', digest_size=16)
        for line in self.allLines:
            hash.update(line.encode('utf-8'))
        self.hexdigest= hash.hexdigest()
        self._about()
        return self.hexdigest

    def save(self, toPath):
        ofile = open(toPath, "w")
        ofile.writelines(self.allLines)
        ofile.close()

    def _about(self):
        self._addLine('# About')
        self._addLine('generated on ' + str(datetime.datetime.now()) + ' with [FrictionlessDarwinCore](https://github.com/frictionlessdata/FrictionlessDarwinCore)')
        self._addLine('secure hash:'+ str(self.hexdigest))

    def _addLine(self, line):
        self.allLines.append(line + '\n\n')

    def _title(self, element):
        self._addLine('# ' + element.text)

    def _element(self, element):
        self._addLine(element.tag + ': '+ element.text)

    def _abstract(self, element):
        if element != None:
            self._addLine('## '+ element.tag)
            for p in element.findall('./para'):
                self._addLine(p.text)

    def _keywords(self, element):
        self._addLine('## Keywords')
        for k in element.findall('./keywordSet'):
            self._addLine('*'+ k.find('./keyword').text + '* ' + k.find('./keywordThesaurus').text)

    def _intellectualRigths(self, element):
        ipr= element.find('./intellectualRights')
        self._addLine('## Intellectual Property Rights')
        if ipr != None:
            self._addLine(ipr.findtext('./para') + ' ['+ ipr.findtext('./para/ulink/citetitle') + ']('+ipr.findtext('./para/ulink') + ')')

    def _geographicCoverage(self, element):
        self._addLine('## Geographic Coverage')
        self._addLine('Description: ' + element.find('./geographicDescription').text)
        self._addLine('BoundingCoordinates: West:' + element.find('./boundingCoordinates/westBoundingCoordinate').text +
            '°, East:' + element.find('./boundingCoordinates/eastBoundingCoordinate').text +
            '°, North:' + element.find('./boundingCoordinates/northBoundingCoordinate').text +
            '°, South:' + element.find('./boundingCoordinates/southBoundingCoordinate').text + '°')

    def _taxonomicCoverage(self, element):
        if element != None:
            self._addLine('## Taxonomic Coverage')
            gtc=element.find('./generalTaxonomicCoverage')
            if gtc != None:
                self._element(gtc)
            self._addLine('### Classification')
            for tc in element.findall('./taxonomicClassification/*'):
                self._element(tc)

    def _maintenance(self, element):
        if element != None:
            self._addLine('## Maintenance')
            self._addLine(element.findtext('./description/para'))
            muf=element.find('./maintenanceUpdateFrequency')
            if muf != None:
                self._element(muf)

    def _methods(self, element):
        if element != None:
            self._addLine('## Methods')
            ms=element.find('./methodStep/description/para')
            if ms != None:
                self._addLine('methodStep: ' + ms.text)
            se=element.find('./sampling/studyExtent/description/para')
            if se != None:
                self._addLine('studyExtent: ' + se.text)
            sd=element.find('./sampling/samplingDescription/para')
            if sd != None:
                self._addLine('samplingDescription: ' + sd.text)

    def _project(self, element):
        if element != None:
            self._addLine('## Project')
        id=element.get('id')
        if id !=None:
            self._addLine('id='+element.get('id'))
        title = element.find('./title')
        if title != None:
            self._element(title)
        self._person(element.find('./personnel'))
        self._abstract(element.find('./abstract'))
        self._abstract(element.find('./funding'))
        sad=element.find('./studyAreaDescription/descriptor/descriptorValue')
        if sad != None:
            self._addLine('## study area description')
            self._addLine(sad.text)
        dd=element.find('./designDescription/description/para')
        if dd != None:
            self._addLine('## design description')
            self._addLine(dd.text)

    def _person(self, element):
        if element != None:
            self._addLine('## ' + element.tag)
            self._addLine('Name:'+element.find('./individualName/givenName').text + ' ' + element.find('./individualName/surName').text)
            org=element.find('./organizationName')
            if org != None:
                self._addLine('Organization:'+ org.text)
            pos=element.find('./positionName')
            if pos != None:
                self._addLine('Position:'+ pos.text)
            email=element.find('./electronicMailAddress')
            if email != None:
                self._addLine('email:'+email.text)
            userid=element.find('./userId')
            if userid != None:
                self._addLine('userId:'+userid.text+ ' ('+ userid.get('directory') + ')')

    def _additionalMetadata(self, element):
        if element != None:
            self._addLine('## Additional Metadata')
            for am in element.findall('./metadata/gbif/*'):
                self._element(am)


if __name__ == '__main__':
        m = DwCMetadata('http://ipt.ala.org.au/eml.do?r=global')
        print(m.document())
        m.save('../tmp/README.md')

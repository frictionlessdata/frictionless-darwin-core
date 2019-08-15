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

        root = ET.parse(self.emlfile).getroot()
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
        self._about()

    def save(self, toPath):
        ofile = open(toPath, "w")
        ofile.writelines(self.allLines)
        ofile.close()

    def _about(self):
        self._add('# About')
        self._add('generated on ' + str(datetime.datetime.now()) + ' with [FrictionlessDarwinCore](https://github.com/frictionlessdata/FrictionlessDarwinCore)')

    def _add(self, line):
        self.allLines.append(line + '\n\n')

    def _title(self, element):
        self._add('# ' + element.text)

    def _element(self, element):
        self._add(element.tag + ': '+ element.text)

    def _abstract(self, element):
        if element != None:
            self._add('## '+ element.tag)
            for p in element.findall('./para'):
                self._add(p.text)

    def _keywords(self, element):
        self._add('## Keywords')
        for k in element.findall('./keywordSet'):
            self._add('*'+ k.find('./keyword').text + '* ' + k.find('./keywordThesaurus').text)

    def _intellectualRigths(self, element):
        ipr= element.find('./intellectualRights')
        self._add('## Intellectual Property Rights')
        if ipr != None:
            self._add(ipr.findtext('./para') + ' ['+ ipr.findtext('./para/ulink/citetitle') + ']('+ipr.findtext('./para/ulink') + ')')

    def _geographicCoverage(self, element):
        self._add('## Geographic Coverage')
        self._add('Description: ' + element.find('./geographicDescription').text)
        self._add('BoundingCoordinates: West:' + element.find('./boundingCoordinates/westBoundingCoordinate').text +
            '°, East:' + element.find('./boundingCoordinates/eastBoundingCoordinate').text +
            '°, North:' + element.find('./boundingCoordinates/northBoundingCoordinate').text +
            '°, South:' + element.find('./boundingCoordinates/southBoundingCoordinate').text + '°')

    def _taxonomicCoverage(self, element):
        if element != None:
            self._add('## Taxonomic Coverage')
            gtc=element.find('./generalTaxonomicCoverage')
            if gtc != None:
                self._add(gtc.tag + ': ' + gtc.text)
            self._add('### Classification')
            for tc in element.findall('./taxonomicClassification/*'):
                self._add(tc.tag + ': ' + tc.text)

    def _maintenance(self, element):
        if element != None:
            self._add('## Maintenance')
            self._add(element.findtext('./description/para'))
            muf=element.find('./maintenanceUpdateFrequency')
            if muf != None:
                self._add(muf.tag + ': ' + muf.text)

    def _methods(self, element):
        if element != None:
            self._add('## Methods')
            ms=element.find('./methodStep/description/para')
            if ms != None:
                self._add('methodStep: ' + ms.text)
            se=element.find('./sampling/studyExtent/description/para')
            if se != None:
                self._add('studyExtent: ' + se.text)
            sd=element.find('./sampling/samplingDescription/para')
            if sd != None:
                self._add('samplingDescription: ' + sd.text)

    def _project(self, element):
        if element != None:
            self._add('## Project')
        self._add('id='+element.get('id'))
        title = element.find('./title')
        if title != None:
            self._add(title.tag + ': '+ title.text)
        self._person(element.find('./personnel'))
        self._abstract(element.find('./abstract'))
        self._abstract(element.find('./funding'))
        sad=element.find('./studyAreaDescription/descriptor/descriptorValue')
        if sad != None:
            self._add('## study area description')
            self._add(sad.text)
        dd=element.find('./designDescription/description/para')
        if dd != None:
            self._add('## design description')
            self._add(dd.text)

    def _person(self, element):
        if element != None:
            self._add('## ' + element.tag)
            self._add('Name:'+element.find('./individualName/givenName').text + ' ' + element.find('./individualName/surName').text)
            org=element.find('./organizationName')
            if org != None:
                self._add('Organization:'+ org.text)
            email=element.find('./electronicMailAddress')
            if email != None:
                self._add('email:'+email.text)

    def _additionalMetadata(self, element):
        if element != None:
            self._add('## Additional Metadata')
            for am in element.findall('./metadata/gbif/*'):
                self._add(am.tag + ': ' + am.text)



if __name__ == '__main__':
#        m = DwCMetadata('../tests/eml.xml')
        m = DwCMetadata('../tests/Data/dwca_S0_eml.xml')
        m.document()
        m.save('../tmp/README.md')

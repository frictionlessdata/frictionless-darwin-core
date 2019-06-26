# Frictionless DarwinCore
A tool that convert [Darwin Core Archive](https://en.wikipedia.org/wiki/Darwin_Core_Archive) into [Frictionless Data Package](https://frictionlessdata.io/specs/data-package/).

## Rationale
**DarwinCore** standard, created and maintained by [Biodivesity Informatics Standards(aka TDWG)](https://www.tdwg.org/), is used to publish Life Sciences data about observations, specimens, species checklists and sampling events. DarwinCore Archive(DwCA), a bundle of biodiversity data and metadata files, is well established standard for publishing or using data in [Global Biodiversity Information Facility](https://www.gbif.org/) and other research networks.

**Frictionless Data Package** is domain agnostic data publication standard that offers a variety of cross technology tools.

Bridging these two data standard ecosystems is the vision guiding this project.

## Introduction
This tool will automatically convert any DwCA into Tabular Data Package.

## Test cases
The [initial test cases](./testCases.md) cover a wide variety of Darwin Core usage. These case should give enough confidence that basic incompatibilities are identified, reported and solved.

## Contributing
You are encouraged to contribute by identifying new issues and helping to solve them.

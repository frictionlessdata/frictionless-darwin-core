# Frictionless Darwin Core
A tool converting [Darwin Core Archive](https://en.wikipedia.org/wiki/Darwin_Core_Archive) into [Frictionless Data Package](https://frictionlessdata.io/specs/data-package/).

## Features
* **datapackage.json**: Ensure your DarwinCore archive complies with [Frictionless specifications](https://frictionlessdata.io/specs/)
* **README.md**: Add human readable metadata from [EML](https://en.wikipedia.org/wiki/Ecological_Metadata_Language)
* **Support all standards [DarwinCore terms](#darwincore-terms)**
* **Support default values in DarwinCore schema**
* **Fields constraints**: Enable further data validation, with [goodtables](https://github.com/frictionlessdata/goodtables-py)
* **URL**: Accept DarwinCore Archive from local path or URL
* **Command line interface**

## Contents
<!--TOC-->
* [Getting Started](#getting-started)
    * [Installing](#installing)
    * [Running on CLI](#running-on-cli)
    * [Python use](#python-use)
* [Documentation](#documentation)
    * [Rationale](#rationale)
    * [What it does?](#what-it-does)
    * [DarwinCore terms](#darwincore-terms)
    * [Test cases suite](#test-cases-suite)
* [Contributing](#contributing)
<!--TOC-->

## Getting Started
### Installing
```
pip install FrictionlessDarwinCore
```

### Running on CLI
```sh
fdwca --help
Usage: fdwca [OPTIONS] DWCA OUTPATH

Options:
  -f, --format [json|md|csv]  Output format
  --help                  Show this message and exit.

# convert from local DwC archive
fdwca myDwC.zip myDP.zip

# convert from URL (archive accessible on internet)
fdwca https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles S1dp.zip

# only generates JSON descriptor (datapackage.json)
fdwca -f json https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles datapackage.json

# only generates markdown human readable metadata (readme.md)
fdwca -f md https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles readme.md

# only converts data as zipped CSV files
fdwca -f csv https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles beetles.zip

```

### Python use
Alternatively, you can use DwCArchive Python object like this:
```python
from FrictionlessDarwinCore import DwCArchive

# load DarwinCore archive from URL
da = DwCArchive('https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles')
# infer Data Package structure from DarwinCore files
da.infer()
if da.valid:
  # save it as Data Package locally
  da.save('BeetlesDP.zip')
  # ... or generates separate JSON descriptor
  da.to_json('datpackage.json')
  # ... or generates separate markdown human readable metadata
  da.to_markdown('readme.md')
  # ... or generated zip with data files only
  da.to_csv('data.zip')
```

## Documentation
### Rationale
**DarwinCore** standard, created and maintained by [Biodivesity Informatics Standards(aka TDWG)](https://www.tdwg.org/), is used to publish Life Sciences data about observations, collections specimens, species checklists and sampling events. DarwinCore Archive(DwCA), a bundle of biodiversity data and metadata files, is well established mechanism for publishing or using data in [Global Biodiversity Information Facility](https://www.gbif.org/) and other Life Sciences networks.

**Frictionless Data Package** is an emerging, domain agnostic, data standard that offers a variety of cross technology tools.

Bridging these two data ecosystems is our vision. This project is supported by [Open Knowledge Foundation](https://okfn.org/) and funded under the [Frictionless Data Tool Fund](https://toolfund.frictionlessdata.io/).

### What it does?
DarwinCore archives consist of:
* a **core** data file
* optionally, 1 or more **extension** data file(s)
* eml.xml: **metadata** written in Ecological Metadata Language
* meta.xml: the **structure** of the DarwinCore data files

Basically, this conversion tool appends two files to the archive, see diagram below:
* **datapackage.json**: data package descriptor of the data files
* **readme.md**: markdown, human readable, metadata

<pre>┌─────────────────────────────────────────────────────────────────┐
│   ┌──────────────────────────────────────────────────────────┐  │
│   │DarwinCore Archive                                        │  │
│   │                                                          │  │
│   │                                ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─       │  │
│   │                           ┌ ─ ─    Extension 1    │      │  │
│   │                                └ ─ ─ ─ ─ ─ ─ ─ ─ ─       │  │
│   │    ┌──────────────────┐   │    ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─       │  │
│   │    │    Core file     │─ ─ ─ ─     Extension 2    │      │  │
│   │    └──────────────────┘   │    └ ─ ─ ─ ─ ─ ─ ─ ─ ─       │  │
│   │                                                          │  │
│   │                           │                              │  │
│   │                                ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─       │  │
│   │                           └ ─ ─    Extension n    │      │  │
│   │                                └ ─ ─ ─ ─ ─ ─ ─ ─ ─       │  │
│   │                                                          │  │
│   │   ┌──────────────────┐         ┌──────────────────┐      │  │
│   │   │     meta.xml     │         │     eml.xml      │      │  │
│   │   └──────────────────┘         └──────────────────┘      │  │
│   │             │                            │               │  │
│   └─────────────┼────────────────────────────┼───────────────┘  │
│                 ▼                            ▼                  │
│       ┌──────────────────┐         ┌──────────────────┐         │
│       │ datapackage.json │         │    readme.md     │         │
│       └──────────────────┘         └──────────────────┘         │
│                                                                 │
│                                           FrictionlessDarwinCore│
│                                                  (=Data Package)│
└─────────────────────────────────────────────────────────────────┘
</pre>
The tool can also generate these two files as separate outputs without touching the archive.

Additionally, the tool also converts the Core and Extension(s) files, when needed.

### DarwinCore terms
Darwin Core is a very persmissive standard some recommandations but almost no constraining rules. This [table](https://github.com/andrejjh/FrictionlessDarwinCore/blob/master/FrictionlessDarwinCore/fdwc_terms.csv) assigns Frictionless Data Package's type, format and constraints to every [Darwin Core term](https://dwc.tdwg.org/terms/).
Values that do not comply with these **Frictionless DarwinCore rules** will automatically raise warnings.

### Test cases suite
The initial [test cases suite](./testCases.md) covers a wide variety of Darwin Core usages. It should give enough confidence that basic incompatibilities are identified, reported and solved but it will not guarantee that all possible DwC Archives will automatically translate into valid Data Packages.

## Contributing
You are encouraged to contribute by identifying/reporting issues or incompatiblities and helping to solve them.

### Not familiar with Darwin Core?
Have a look at iDigBio's [Darwin Core Hour](https://www.idigbio.org/content/darwin-core-hour-webinar-series) Webinar Series.

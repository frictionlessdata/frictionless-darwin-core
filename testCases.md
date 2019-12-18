# Initial test cases

The following datasets act as test cases for the Frictionless Darwin Core conversion tool.
They offer a diversity of cores: **Occurrence**, **Checklist** and **Event** and support basic to most advanced uses of the DwC star schema with no, one or many extensions. Some are build by GBIF's IPT, others by other publishing tool such as BioCASE or Scratchpads.

## Simple cases
* S0:[Reef Life Survey: Global reef fish dataset](https://www.gbif.org/dataset/38f06820-08c5-42b2-94f6-47cc3e83a54a),
Metadata only [(EML)](http://ipt.ala.org.au/eml.do?r=global)
* S1:[Collection of saproxylic and xylobiont Beetles](https://www.gbif.org/dataset/d3d38190-0c13-11df-b8c6-b8a03c50a862)
Occurrence core, no extension [(DwCA)](https://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles)
* S2: [Afromoths, online database of Afrotropical moth species (Lepidoptera)](https://www.gbif.org/dataset/65c9103f-2fbf-414b-9b0b-e47ca96c5df2)
Checklist core, no extension [(DwCA)](https://ipt.biodiversity.be/archive.do?r=afromoths)
* S3: [AxIOM: Amphipod crustaceans from insular Posidonia oceanica seagrass meadows](https://www.gbif.org/dataset/b146a93c-657b-4768-aa51-9cabe3dac808)
Event core + Occurrence extension [(DwcA)](https://ipt.biodiversity.be/archive.do?r=axiom)

## Complex cases
* C1: [Meise Botanic Garden Herbarium (BR)](https://www.gbif.org/dataset/b740eaa0-0679-41dc-acb7-990d562dfa37) by Botanic Garden Meise
Occurrence core + multimedia extension, large file, 1 GB of uncompressed data with 1.7 Mio records [(DwCA)](http://apm-ipt.br.fgov.be:8080/ipt-2.3.5/archive.do?r=botanical_collection)
* C2:[Phytoplankton-BG Black Sea-2007-2016](https://obis.org/dataset/d9a55b00-17d0-471b-bd49-6f97c8a08f1f) by OBIS
Event core + 2 extensions (ExtendedMeasurementOrFact & Occurrence) [(DwcA)](http://gp.sea.gov.ua:8082/ipt/archive.do?r=phyto2016-37)
* C3: [Empidoid flies from Cabo Verde (Diptera, Empidoidea, Dolichopodidae and Hybotidae) are not only composed of Old World tropical species](http://tb.plazi.org/GgServer/dwca/FFF2FF91FFD8FF8818250D59B410FF9B.zip) by PLAZI
Checklist core + 7 extensions [(DwcA)](http://tb.plazi.org/GgServer/dwca/FFF2FF91FFD8FF8818250D59B410FF9B.zip)


## Data cases
These datasets contain default values and therefore necessitate data conversion:
* D1: [Lice (Phthiraptera) of Ireland](https://www.gbif.org/dataset/6e21cfd9-34ed-4983-bab4-0e912a5770bd), Occurrence Core  [(DwcA)](http://gbif.biodiversityireland.ie/LiceOfIreland.zip)
* D2: [The Great Koaloa Count South Australia]
[(DwcA)](https://biocache.ala.org.au/archives/gbif/dr1008/dr1008.zip)


## Tricky cases
* T1: [The Brown University Foraminiferal Data Base (BFD)](https://www.gbif.org/dataset/68efc55e-f762-11e1-a439-00145eb45e9a) Occurrence dataset by Pangeae [(DwcA)](http://digir.pangaea.de/dwca/?id=96900)
* T2: [Database for alien invasive plants occurrences in Germany](https://www.gbif.org/dataset/f0c74a2c-4bd8-49d0-837a-92bb835fd2f3) Occurrence, BioCASE dataset [(DwcA)](http://85.214.43.90/biocase/downloads/korina/Database%20for%20alien%20invasive%20plants%20occurrences%20in%20Germany.DwCA.zip)
* T3: [AfriBats](https://www.gbif.org/dataset/5af9dd93-3a27-43b6-afea-bf8a3bca5dc9) Checklist dataset by Scratchpads [(DwcA)](http://afribats.myspecies.info/gbif-dwca.zip)
* T4: [Naturalis Biodiversity Center (NL) - Amphibia and Reptilia](https://www.gbif.org/dataset/fccafd83-a934-4021-a112-4ae5fd39c14b) Occurrence dataset by Naturalis [(DwcA)](http://api.biodiversitydata.nl/v2/specimen/dwca/getDataSet/amphibia-and-reptilia)

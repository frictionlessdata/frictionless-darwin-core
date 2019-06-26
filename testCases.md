# Initial test cases

The following datasets will act as test cases for the Frictionless Darwin Core conversion tool.
They offer a diversity of cores: **Occurrence**, **Checklist** and **Event** and support basic to most advanced uses of the DwC star schema with no, one or many extensions. The first one has no data, only metadata. The last one has 8 data files(core+7 extensions).
All except the last one are build with GBIF's IPT.

## Simple cases
* S0:[Inventaire et dénombrement des oiseaux du Parc Naturel Communautaire de la Vallée du Sitatunga (Sud Bénin)](https://www.gbif.org/dataset/3194e21c-447a-410d-bb09-31398482de1f)
Metadata only
* S1:[Collection of saproxylic and xylobiont Beetles](https://www.gbif.org/dataset/d3d38190-0c13-11df-b8c6-b8a03c50a862)
Occurrence core, no extension
* S2: [Afromoths, online database of Afrotropical moth species (Lepidoptera)](https://www.gbif.org/dataset/65c9103f-2fbf-414b-9b0b-e47ca96c5df2)
Checklist core, no extension
* S3: [AxIOM: Amphipod crustaceans from insular Posidonia oceanica seagrass meadows](https://www.gbif.org/dataset/b146a93c-657b-4768-aa51-9cabe3dac808)
Event core + Occurrence extension

## Complex cases
* C1: [Meise Botanic Garden Herbarium (BR)](https://www.gbif.org/dataset/b740eaa0-0679-41dc-acb7-990d562dfa37) by Botanic Garden Meise
Occurrence core + multimedia extension, large file, 1 GB of uncompressed data with 1.7 Mio records
* C2:[Phytoplankton-BG Black Sea-15AK2007132](http://gp.sea.gov.ua:8082/ipt/resource?r=ak2007-00) by OBIS
Event core + 2 extensions (MeasurementOrFact & Occurrence)
* C3: [Empidoid flies from Cabo Verde (Diptera, Empidoidea, Dolichopodidae and Hybotidae) are not only composed of Old World tropical species](http://tb.plazi.org/GgServer/dwca/FFF2FF91FFD8FF8818250D59B410FF9B.zip) by PLAZI
Checklist core + 7 extensions

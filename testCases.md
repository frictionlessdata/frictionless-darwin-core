# Initial test cases

The following datasets will act as test cases for the Frictionless Darwin Core conversion tool.
They offer a diversity of cores: **Occurrence**, **Checklist** and **Event** and support basic to most advanced uses of the DwC star schema with no, one or many extensions. The first one has no data, only metadata. The last one has 8 data files(core+7 extensions).
All except the last one are build with GBIF's IPT.

## Simple case
* S0:[Inventaire et dénombrement des oiseaux du Parc Naturel Communautaire de la Vallée du Sitatunga (Sud Bénin)](https://www.gbif.org/dataset/3194e21c-447a-410d-bb09-31398482de1f)
Metadata only
* S1:[Collection of saproxylic and xylobiont Beetles](http://ipt.biodiversity.be/archive.do?r=rbins_saproxilyc_beetles)
Occurrence core
* S2: [Afromoths, online database of Afrotropical moth species (Lepidoptera)](http://ipt.biodiversity.be/archive.do?r=afromoths)
Checklist core
* S3: [AxIOM: Amphipod crustaceans from insular Posidonia oceanica seagrass meadows](http://ipt.biodiversity.be/archive.do?r=axiom)
Event core + occurrence extension

## Complex DwCAs
* C1: [Meise Botanic Garden Herbarium (BR)](http://apm-ipt.br.fgov.be:8080/ipt-2.3.5/archive.do?r=botanical_collection)
Occurrence core + multimedia extension, large file, 1 GB of uncompressed data with 1.7 Mio records
* C2:[Phytoplankton-BG Black Sea-15AK2007132](http://gp.sea.gov.ua:8082/ipt/resource?r=ak2007-00) by OBIS
Event core + 2 extensions: MeasurementOrFact & Occurrence
* C3: [Empidoid flies from Cabo Verde (Diptera, Empidoidea, Dolichopodidae and Hybotidae) are not only composed of Old World tropical species](http://tb.plazi.org/GgServer/dwca/FFF2FF91FFD8FF8818250D59B410FF9B.zip) by PLAZI
Checklist core + 7 extensions

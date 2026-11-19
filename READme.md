# Code for *Digital Archives of Science*

Scripts used to collect and analyse metadata from digital collections of
scientific heritage, for the PhD thesis *Querying the Digital Archive of
Science* (EPFL, 2024) and the book:

- Alina Volynskaya, *Digital Archives of Science: Revisiting the Vestiges of
  Knowledge-Making* (De Gruyter Oldenbourg, 2026),
  https://doi.org/10.1515/9783111729664
- Dataset: https://doi.org/10.5281/zenodo.16411455

## Contents

| File | Collection | Method |
|---|---|---|
| `CSHL.py` | Cold Spring Harbor Laboratory Library | HTML scraping |
| `babbage.py` | Charles Babbage Institute (UMedia) | JSON API |
| `cern_video.py` | CERN Document Server, videos | HTML scraping |
| `fitzerald.py` | Royal Dublin Society digital archive | HTML scraping |
| `pauling.py` | Linus Pauling Research Notebooks | HTML scraping |
| `correspondence_analysis.R` | 118 digital collections | Correspondence analysis (FactoMineR) |

The Python scripts harvest subject terms (tags, keywords, subject headings)
and write them to CSV. The R script maps how the collections organise and
contextualise their items, using a presence/absence matrix of nine modes
of organisation.

## Requirements

Python 3: `requests`, `beautifulsoup4`, `html5lib`, `nltk`
R: `FactoMineR`, `factoextra`, `ggrepel`

## Note

The scripts were written in 2020–2022 for the page structures of these
collections at the time; some sites may have changed since.

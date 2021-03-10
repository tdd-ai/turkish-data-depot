# Turkish Data Depot 

In this repo, Turkish Data Depot (TDD) datasets' sharing formats, and metadata designs will be shared and updated.  

## Datasets Meta fields (v0.1)

|field|value-type|value|
|---|---|---|
|catalog|id|XYZ-C-2020-CCBY-00|
|type|type::enum|corpus|
|name|string|BOUN Web Derlemi|
|license|license::enum|cc-by-sa-4.0|
|release-date|int|2008|
|download-size|int|4.3GB|
|authors|list[string]|Department of Computer Engineering, Bogaziçi University|
|format|string|XML|
|data-type|list[data-type::enum]|text|
|annotation|annotation::enum|available|
|citation|string|https://arxiv.org/abs/1810.04805|
|source|source::enum|web-collection|
|compression|compression::enum|tar.gz|
|website|string|https://dumps.wikimedia.org/|
|doi|string|https://doi.org/10.35111/fr89-3285|
|description|string|Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.|

### Enumeration definitions

#### **type::enum**

|value|description|
|---|---|
|corpus|unannotated text corpus of any format|
|parallel-corpus|aligned translations of text of two languages or more|
|morphology-tagged-corpus|PoS tagged, lemmatized, morphologically disambiguated text|
|treebank|turkish wordnet etc..|
|dictionary|dictionary|
|lexicon|lexicon, a set of vocabulary|
|word-vectors|set of pretrained word vectors|
|language-model|pretrained weights of language model|
|morphology-model|software or model for morphological anaylsis|
|parser|software or model for dependency parsing|
|machine-translation-model|software or model|
|nlp-toolkit|toolkit for turkish/generic nlp|
|ner-tagger|named entity recognition tagging software or model|
|rdf-triples|rdf triples, knowledge graphs and information retrieval|

#### **data-type::enum**

|value|description|
|---|---|
|text|raw or annotated text|
|video|short/long videos|
|image|visual files|
|audio|audio|

#### **annotation::enum**

|value|description|
|---|---|
|raw-text|Unannotated|
|tokenized-word-perline|Tokenized with a format that has a word for every line|
|tokenized-whitespace|Tokenized with a format that is seperated to units including punctiation marks|
|sentenced-marked|Starting and ending of the sentences are marked|
|pos-tagged|word types are tagged|
|morphologically-annotated|contains Morpheme tag|
|dependency-annotation|contains Dependency analyse information tag|
|syntactically-annotated|tagged at Syntactical level|
|statistics|Contains statistical information| 

#### **source::enum**

|value|description|
|---|---|
|varied|varied sources|
|wiki|includes all types of wikis|
|news-paper|online news resource|
|academic|using research papers online|
|books|using online books|
|user-generated|reviews or comments of internet users (amazon, imdb etc.)|
|social-media|twitter tweets|
|emails|sent emails|
|dialog|short messages sms or chats|
|web-collection|crawled from web which can contain extracted or raw web pages|

#### **compression::enum**

|value|description|
|---|---|
|.tar.gz|tarball with gzip|
|.gz|gzip|
|.tar|tarball|
|.zip|zip|
|.bz2|bzip2|


#### **license::enum**

|value|description|
|---|---|
|afl-3.0|Academic Free License v3.0|
|apache-2.0|Apache license 2.0|
|artistic-2.0|Artistic license 2.0|
|bsl-1.0|Boost Software License 1.0|
|bsd-2-clause|BSD 2-clause "Simplified" license|
|bsd-3-clause|BSD 3-clause "New" or "Revised" license|
|bsd-3-clause-clear|BSD 3-clause Clear license|
|cc|Creative Commons license family|
|cc0-1.0|Creative Commons Zero v1.0 Universal|
|cc-by-4.0|Creative Commons Attribution 4.0|
|cc-by-sa-4.0|Creative Commons Attribution Share Alike 4.0|
|wtfpl|Do What The F*ck You Want To Public License|
|ecl-2.0|Educational Community License v2.0|
|epl-1.0|Eclipse Public License 1.0|
|epl-2.0|Eclipse Public License 2.0|
|eupl-1.1|European Union Public License 1.1|
|agpl-3.0|GNU Affero General Public License v3.0|
|gpl|GNU General Public License family|
|gpl-2.0|GNU General Public License v2.0|
|gpl-3.0|GNU General Public License v3.0|
|lgpl|GNU Lesser General Public License family|
|lgpl-2.1|GNU Lesser General Public License v2.1|
|lgpl-3.0|GNU Lesser General Public License v3.0|
|isc|ISC|
|lppl-1.3c|LaTeX Project Public License v1.3c|
|ms-pl|Microsoft Public License|
|mit|MIT|
|mpl-2.0|Mozilla Public License 2.0|
|osl-3.0|Open Software License 3.0|
|postgresql|PostgreSQL License|
|ofl-1.1|SIL Open Font License 1.1|
|ncsa|University of Illinois/NCSA Open Source License|
|unlicense|The Unlicense|
|zlib|zLib License|


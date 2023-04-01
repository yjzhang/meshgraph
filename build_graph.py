# TODO: construct a meshgraph
import os

import pubmed_parser as pp


MEDLINE_PATH = '/media/yjzhang/easystore-5gb-1/research_big_data/pubmed_abstracts'
GENE2PUBMED_PATH = '/media/yjzhang/easystore-5gb-1/research_big_data/ncbi/gene2pubmed'
TAXIDS = {'human': 9606, 'mouse': 10090, 'worm': 6239}

# 1. parse gene2pubmed

for filename in os.listdir(MEDLINE_PATH):
    pass

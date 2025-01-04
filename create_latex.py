#!/usr/bin/env python

import subprocess
import argparse

parser = argparse.ArgumentParser(description='Create pdf with bibliography',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='example: create_latex bibtex_2016-02-07.bib')
parser.add_argument('bibtex')
parser.add_argument('--title', default='List of publications', help='Title of the document')
parser.add_argument('--author', default=None, help='Author of the document')

args = parser.parse_args()

TEMPLATE_FILENAME = "template_latex.tex"
with open(TEMPLATE_FILENAME) as f:
    template = f.read()

template = template.replace("ADD_BIBTEX_HERE", args.bibtex)
template = template.replace("ADD_TITLE_HERE", args.title)
if args.author:
    template = template.replace("ADD_AUTHOR_HERE", args.author)
else: 
    template = template.replace("\\author{ADD_AUTHOR_HERE}", "")

with open('publications.tex', 'w') as f:
    f.write(template)

subprocess.call(['pdflatex', 'publications.tex'])
subprocess.call(['bibtex', 'publications.aux'])
subprocess.call(['pdflatex', 'publications.tex'])
subprocess.call(['pdflatex', 'publications.tex'])

print("output written in publications.pdf")

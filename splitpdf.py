#!/usr/bin/env python
#http://unix.stackexchange.com/questions/12482/split-pages-in-pdf
# and for joining them, see:
# http://stackoverflow.com/questions/2507766/merge-convert-multiple-pdf-files-into-one-pdf
import copy, sys
from pyPdf import PdfFileWriter, PdfFileReader
input = PdfFileReader(sys.stdin)
output = PdfFileWriter()
for p in [input.getPage(i) for i in range(0,input.getNumPages())]:
    q = copy.copy(p)
    (w, h) = p.mediaBox.upperRight
    p.mediaBox.upperRight = (w/2, h)
    q.mediaBox.upperLeft = (w/2, h)
    output.addPage(p)
    output.addPage(q)
output.write(sys.stdout)

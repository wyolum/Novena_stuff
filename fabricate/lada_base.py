from sys import path
path.append('../../Lada/fabricate') ## add lada library path
from lada import *

### main enclosure
T = 3* mm
main_LENGTH = 8 * inch + 2 * T
main_WIDTH = 135 * mm + 2 * T
main_HEIGHT = 35 * mm + 2 * T
can = new_canvas("Novena_lada.pdf", 20*inch, 12*inch, .5*inch)
main_lada = Lada(main_LENGTH, main_WIDTH, main_HEIGHT, T, max_edge_span=200*mm)
main_lada.drawOn(can)
can.save()
print 'wrote', can._filename
main_scad = main_lada.toScad(name='main')
scadfile = open("Novena_lada.scad", 'w')
print >> scadfile, main_scad
print 'wrote', scadfile.name


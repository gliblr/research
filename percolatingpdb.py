import math
import datetime
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

title = '***************************************\n     Percolating Network Tester\n              version 1\n     ' + __date__ + '\n***************************************\n'
print title
inputpdb = raw_input("What is the name of the PDB file to analyze? ")
input = open(inputpdb, "r")

natoms = 0
cutoff = 150
r = 0
master = []
neighbors = 0
neighbortable = []
xdim = 0
ydim = 0
zdim = 0

for line in input:
  if line[0:4]=='ATOM':
    res = line[17:21]
    atom = line[13:16]
    x = float(line[30:38])
    y = float(line[38:46])
    z = float(line[46:54])
    q = float(line[61:66])
    list = [x,y,z,q,res,atom]
    natoms = natoms + 1
    master.append(list)
  elif line[0:4]=='CRYS':
    xdim = float(line[7:15])
    ydim = float(line[15:24])
    zdim = float(line[24:33])

i = 0
bonds = 0
while i < natoms:
    x1 = master[i][0]
    y1 = master[i][1]
    z1 = master[i][2]
    j = i + 1
    while j < natoms:
        x2 = master[j][0]
        y2 = master[j][1]
        z2 = master[j][2]
        sdx = (x1-x2)*(x1-x2)
        sdy = (y1-y2)*(y1-y2)
        sdz = (z1-z2)*(z1-z2)
        r = sdx + sdy + sdz
        if r != 0 and r <= cutoff:
#            print 'NEIGHBOR FOUND', i, j, r, sdx, sdy, sdz
            table = [i, j, sdx, sdy, sdz]
            neighbortable.append(table)
            bonds = bonds + 1
        j = j + 1
    i = i + 1
#    print i, '/', natoms

#print neighbortable

chainnumber = -1
chain = []
chaintable = []
i = 0
while i < bonds:
    a = neighbortable[i][0]
    b = neighbortable[i][1]
    if chaintable.count(a) == 0 and chaintable.count(b) == 0:
        chainnumber = chainnumber + 1
        chain.append(a, b)
        chaintable[chainnumber].append(chain)
        print "NEW CHAIN in Chaintable #", chainnumber
    if chaintable.count(a) != 0 and chaintable.count(b) == 0:
        print chaintable.index(a)

#    j = 0
#    while j < bonds:
#        b = neighbortable[j][0]
#        c = neighbortable[j][1]
##        print 'A=',a, 'B=',b, 'C=',c, chain.count(a), chain.count(b), chain.count(c)
#        if a==b and chain.count(c) == 0:
#            if chain.count(a) == 0 and chaintable.count(a) == 0:
#                chain.append(b)
#                print i, j, a, b, c, 'NEW CHAIN Appended ', a, 'as A'
#                chainnumber = chainnumber + 1
#                chaintable.append(chain)
#                chain = []
#            chain.append(c)
#            print i, j, a, b, c, 'Appended ', c, 'as C'
#        if a!=b and chain.count(b) == 1 and chain.count(c) == 0:
#            chain.append(c)
#            print i, j, a, b, c, 'Appended ', c, 'C due to B'
#        j = j + 1
#    i = i + 1
#print chaintable
#print chainnumber
#    print i, '/', natoms



#print 'Percolating?', percol

import math
from decimal import *

__author__="galibaler"
__date__ ="$Nov 28, 2012 8:21:45 AM$"

print '***************************************'
print '     Electrostatic Ewald Summation'
print '***************************************'

#inputpdb = raw_input("What is the name of the PDB file to analyze? ")
inputpdb = "GRASPnoionsconnelly.pdb"
input = open(inputpdb, "r")
atoms = 0
cutoff = 9.0
r = 0
master = []
xdim = 0
ydim = 0
zdim = 0

for line in input:
  if line[0:4]=='ATOM':
    res = line[17:21]
    x = float(line[31:38])
    y = float(line[39:46])
    z = float(line[47:54])
    q = float(line[61:66])
    list = [x,y,z,q,res]
    atoms = atoms + 1
    master.append(list)
  elif line[0:4]=='CRYS':
    xdim = float(line[7:15])
    ydim = float(line[15:24])
    zdim = float(line[24:33])

i = 0
potsum = 0
while i < atoms:
    j = 0
    atomsum = 0
    neighbor = 0
    x1 = master[i][0]
    y1 = master[i][1]
    z1 = master[i][2]
    q1 = master[i][3]
    if master[i][4] == 'DOT ': #Check to see if atom is on connelly dot surface
        while j < atoms:
            if master[j][4] != 'DOT ':
                x2 = master[j][0]
                x2a = x2 + xdim
                x2b = x2 - xdim
                y2 = master[j][1]
                y2a = y2 + ydim
                y2b = y2 - ydim
                z2 = master[j][2]
                z2a = z2 + zdim
                z2b = z2 - zdim
                q2 = master[j][3]
                sdx1 = (x1-x2)*(x1-x2)
                sdxa = (x1-x2a)*(x1-x2a)
                sdxb = (x1-x2b)*(x1-x2b)
                sdy1 = (y1-y2)*(y1-y2)
                sdya = (y1-y2a)*(y1-y2a)
                sdyb = (y1-y2b)*(y1-y2b)
                sdz1 = (z1-z2)*(z1-z2)
                sdza = (z1-z2a)*(z1-z2a)
                sdzb = (z1-z2b)*(z1-z2b)
                r0 = sdx1 + sdy1 + sdz1
                rxa = sdxa + sdy1 + sdz1
                rxb = sdxb + sdy1 + sdz1
                rya = sdx1 + sdya + sdz1
                ryb = sdx1 + sdyb + sdz1
                rza = sdx1 + sdy1 + sdza
                rzb = sdx1 + sdy1 + sdzb
                r = [r0, rxa, rxb, rya, ryb, rza, rzb]
                if min(r) != 0:
                    if min(r) <= cutoff:
                        neighbor = neighbor + 1
                        atomsum = atomsum + q2/min(r)
                        print 'q2', q2, ' r', min(r)
                        print "interaction", i+1, "x", j+1," sum = ", atomsum
            j = j + 1
        potsum = potsum + atomsum
        print i, " neighbors =", neighbor, " atompot =", atomsum, " total potsum = ", potsum
    i = i + 1
    print i, '/', atoms

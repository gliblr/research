import math
import datetime
import sys
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

title = '***************************************\n     Electrostatic Potential Summation\n              version 3\n     ' + __date__ + '\n***************************************\n'
print title
inputpdb = raw_input("What is the name of the PDB file to analyze? ")
#inputpdb = "CDimerS1_4000.pdb"
outputpdb = "OUT" + inputpdb
input = open(inputpdb, "r")
fout = open(outputpdb, "w")
demoatom = 1
atoms = 0
surfdist = 9.0
cutoff = 100.0
r = 0
master = []
surfatm = []
xdim = 0
ydim = 0
zdim = 0

fout.write(title)

for line in input:
  if line[0:4]=='ATOM':
    res = line[17:21]
    atom = line[13:14]
    if atom != 'C' and atom != 'H' and atom != 'O' and atom != 'N' and atom != 'S' and res != 'DOT ':
        atom = 'H'
    x = float(line[31:38])
    y = float(line[39:46])
    z = float(line[47:54])
    q = float(line[61:66])
    list = [x,y,z,q,res,atom]
    atoms = atoms + 1
    master.append(list)
  elif line[0:4]=='CRYS':
    xdim = float(line[7:15])
    ydim = float(line[15:24])
    zdim = float(line[24:33])

i = 0
potsum = 0
input = open(inputpdb, "r")
for line in input:
    if line[0:4]!='ATOM':
        print line[0:69],
        fout.write(line[0:69])
    if line[0:4]=='ATOM':
        j = 0
        atomsum = 0
        neighbor = 0
        issurface = 0.00
        x1 = master[i][0]
        y1 = master[i][1]
        z1 = master[i][2]
        q1 = master[i][3]
        if master[i][4] != 'DOT ' and master[i][4] != 'SOL ' and master[i][4] !='CL- ' and i+1 <= 9336: #Check to see if atom is not protein
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
                        excludedvolume = 0
                        if master[i][5] == 'C' and master[i][4] != 'CL- ':
                            excludedvolume = excludedvolume + 1.7
                        if master[i][5] == 'C' and master[i][4] == 'CL- ':
                            excludedvolume = excludedvolume + 1.75
                        if master[i][5] == 'H':
                            excludedvolume = excludedvolume + 1.0
                        if master[i][5] == 'O':
                            excludedvolume = excludedvolume + 1.5
                        if master[i][5] == 'N':
                            excludedvolume = excludedvolume + 1.6
                        if master[i][5] == 'S':
                            excludedvolume = excludedvolume + 1.8
                        if master[j][5] == 'C' and master[j][4] != 'CL- ':
                            excludedvolume = excludedvolume + 1.7
                        if master[j][5] == 'C' and master[j][4] == 'CL- ':
                            excludedvolume = excludedvolume + 1.75
                        if master[j][5] == 'H':
                            excludedvolume = excludedvolume + 1.0
                        if master[j][5] == 'O':
                            excludedvolume = excludedvolume + 1.5
                        if master[j][5] == 'N':
                            excludedvolume = excludedvolume + 1.6
                        if master[j][5] == 'S':
                            excludedvolume = excludedvolume + 1.8
                        if min(r) >= excludedvolume and min(r) <= cutoff:
                            neighbor = neighbor + 1
                            surfatm.append(j+1)
                            atomsum = atomsum + q2/min(r)
#                            print "interaction", i+1, "-", master[i][4], "x", j+1, "-",master[j][4], 'q2', q2, ' r', min(r), "sum =", atomsum
                            if master[j][4] == 'SOL ' and min(r) <= surfdist:
#                                print "CLOSE WATER MOLECULE NEIGHBOR FOUND!!!!"
                                issurface = 1.00
                j = j + 1
            if issurface == 1.00:
                potsum = potsum + atomsum
#                print "ATOMSUM ADDED TO POTSUM"
#            print i, "neighbors =", neighbor, "atompot =", atomsum, "total potsum =", potsum
#            print atomsum, "issurface", issurface
            if atomsum < 0:
                string = '{0:2.2f}'.format(atomsum)
            else:
                string = ' {0:2.2f}'.format(atomsum)
            print line[0:55] + string + ' {0:2.2f}'.format(issurface)
            fout.write(line[0:55] + string + ' {0:2.2f}'.format(issurface) + '\n')
        else:
            print line[0:56] + '0.00 0.0'
            fout.write(line[0:55] + string + ' {0:2.2f}'.format(issurface) + '\n')
        i = i + 1

#        print i, '/', atoms
print 'Total Potential', potsum
fout.write('{0:2.6f}'.format(potsum))
fout.close()

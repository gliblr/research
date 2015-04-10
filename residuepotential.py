import math
import datetime
import sys
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

title = '***************************************\n  Residue Potential Summation \n              version 3\n     ' + __date__ + '\n***************************************\n'
print title
inputpdb = raw_input("What is the name of the PDB file to analyze? ")
#input = open("OUT2CDimerT1_500.pdb", "r")
outputpdb = "RESSUM" + inputpdb
input = open(inputpdb, "r")
fout = open(outputpdb, "w")
master = []
oldresindex = 0
oldres = "ASP"
p = 0
i = 0
for line in input:
  i = i + 1
  if line[0:4]=='ATOM':
    nres = line[17:21]
    atom = line[13:14]
    if i < 30000:
        newresindex = int(line[23:27])
        if atom != 'C' and atom != 'H' and atom != 'O' and atom != 'N' and atom != 'S' and nres != 'DOT ':
            atom = 'H'
        if nres != 'DOT ' and nres != 'SOL ' and nres != 'CL- ' and nres == 'ASP ' or nres == 'HISH' or nres == 'LYSH' or nres == 'GLU ' or nres == 'ARG ': #Check to see if atom is not protein and only charged residue
            surf = float(line[61:64])
            if newresindex == oldresindex and surf == 1:
#                print float(line[55:60]), "before!", p
                p = p + float(line[55:60])
#                print float(line[55:60]), "after!", p
            elif newresindex != oldresindex:
                if oldresindex != 0:
                    if p < 0.00001 and p > -0.00001:
                        p = 0.0
#                    print oldresindex, " ", oldres, " ", p
                    list = [oldresindex, p]
                    master.append(list)
                p = float(line[55:60])*surf
                oldres = nres
                oldresindex = newresindex

#print oldresindex, " ", oldres, " ", p
list = [oldresindex, p]
master.append(list)
list = [999999, 999999]
master.append(list)

input = open(inputpdb, "r")
i = 0
resno = 0
for line in input:
    if line[0:4]!='ATOM' or line[17:21] == 'SOL ' or line[17:21] == 'CL- ':
        print line[0:69],
        fout.write(line[0:69])
    elif line[0:4]=='ATOM':
        nres = line[17:21]
        resindex = int(line[23:27])
        if master[resno+1][0] == resindex:
            resno = resno + 1
        if nres != 'DOT ' and nres != 'SOL ' and nres != 'CL- ' and nres == 'ASP ' or nres == 'HISH' or nres == 'LYSH' or nres == 'GLU ' or nres == 'ARG ': # and i+1 <= 18672: #Check to see if atom is not protein
            resno = resno + 1
#            print resno
            newp = master[resno-1][1]
            resno = resno - 1
            if newp < 0:
                string = '{0:2.2f}'.format(newp)
            else:
                string = ' {0:2.2f}'.format(newp)
            print line[0:55] + string + line[60:69]
            fout.write(line[0:55] + string + line[60:69])
        else:
            print line[0:56] + '0.00 0.0'
            fout.write(line[0:55] + string + line[60:69])
    i = i + 1

fout.close()

import math
import datetime
import sys
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

#title = '***************************************\n  Electrostatic Potential Difference Collector\n              version 3\n     ' + __date__ + '\n***************************************\n'
#print title
#inputpdb = raw_input("What is the name of the PDB 1 file to analyze? ")
input = open("SQRTOUTCDimerT1_500.pdb", "r")
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
    if i < 20000:
        newresindex = int(line[23:27])
        if atom != 'C' and atom != 'H' and atom != 'O' and atom != 'N' and atom != 'S' and nres != 'DOT ':
            atom = 'H'
        if nres != 'DOT ' and nres != 'SOL ' and nres != 'CL- ': #remove this segment# and nres == 'ASP ' or nres == 'HISH' or nres == 'LYSH' or nres == 'GLU ' or nres == 'ARG ': #Check to see if atom is not protein and only charged residue
            surf = float(line[61:64])
            if newresindex == oldresindex and surf == 1:
#                print float(line[55:60]), "before!", p
                p = p + float(line[55:60])
#                print float(line[55:60]), "after!", p
            elif newresindex != oldresindex:
                if oldresindex != 0:
                    if p < 0.00001 and p > -0.00001:
                        p = 0.0
                    print oldresindex, " ", oldres, " ", p
                p = float(line[55:60])*surf
                oldres = nres
                oldresindex = newresindex

print oldresindex, " ", oldres, " ", p

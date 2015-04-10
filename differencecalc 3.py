import math
import datetime
import sys
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

title = '***************************************\n  Electrostatic Potential Difference Calculator\n              version 3\n     ' + __date__ + '\n***************************************\n'
print title
inputpdb1 = raw_input("What is the name of the PDB 1 file to analyze? ")
inputpdb2 = raw_input("What is the name of the PDB 2 file to analyze? ")
#inputpdb = "CDimerT1_100.pdb"
outputpdb = "DIFFOUT" + inputpdb2
input1 = open(inputpdb1, "r")
input2 = open(inputpdb2, "r")
fout = open(outputpdb, "w")
atoms1 = 0
atoms2 = 0
master1 = []
master2 = []
xdim1 = 0
ydim1 = 0
zdim1 = 0
xdim2 = 0
ydim2 = 0
zdim2 = 0

fout.write(title)

for line in input1:
  if line[0:4]=='ATOM':
    res = line[17:21]
    atom = line[13:14]
    if atom != 'C' and atom != 'H' and atom != 'O' and atom != 'N' and atom != 'S' and res != 'DOT ':
        atom = 'H'
    x = float(line[31:38])
    y = float(line[39:46])
    z = float(line[47:54])
    p = float(line[55:60])
    list1 = [x,y,z,p,res,atom]
    atoms1 = atoms1 + 1
    master1.append(list1)
  elif line[0:4]=='CRYS':
    xdim1 = float(line[7:15])
    ydim1 = float(line[15:24])
    zdim1 = float(line[24:33])

for line in input2:
  if line[0:4]=='ATOM':
    res = line[17:21]
    atom = line[13:14]
    if atom != 'C' and atom != 'H' and atom != 'O' and atom != 'N' and atom != 'S' and res != 'DOT ':
        atom = 'H'
    x = float(line[31:38])
    y = float(line[39:46])
    z = float(line[47:54])
    p = float(line[55:60])
    list2 = [x,y,z,p,res,atom]
    atoms2 = atoms2 + 1
    master2.append(list2)
  elif line[0:4]=='CRYS':
    xdim2 = float(line[7:15])
    ydim2 = float(line[15:24])
    zdim2 = float(line[24:33])

if atoms1!=atoms2:
    print("Atom Number Mismatch!")

i = 0
potsum = 0
input2 = open(inputpdb2, "r")
for line in input2:
    if line[0:4]!='ATOM':
        print line[0:69],
        fout.write(line[0:69])
    if line[0:4]=='ATOM':
        if master2[i][4] != 'DOT ' and master2[i][4] != 'SOL ' and master2[i][4] != 'CL- ' and i+1 <= 18672: #Check to see if atom is not protein
            newp = master2[i][3] - master1[i][3]
            potsum = potsum + newp
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

print ' /n ' + 'Total Potential Difference', potsum
fout.write('{0:2.6f}'.format(potsum))
fout.close()

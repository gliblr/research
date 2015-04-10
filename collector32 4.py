import math
import datetime
import sys
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

title = '***************************************\n      PDB 32 Way DOT File Combiner\n              version 3\n     ' + __date__ + '\n***************************************\n'
print title
inputpdb1 = "OUTS1CCON2FBSA5nm10.pdb"
inputpdb2 = "OUTS2CCON2FBSA5nm10.pdb"
inputpdb3 = "OUTS3CCON2FBSA5nm10.pdb"
inputpdb4 = "OUTS4CCON2FBSA5nm10.pdb"
inputpdb5 = "OUTS5CCON2FBSA5nm10.pdb"
inputpdb6 = "OUTS6CCON2FBSA5nm10.pdb"
inputpdb7 = "OUTS7CCON2FBSA5nm10.pdb"
inputpdb8 = "OUTS8CCON2FBSA5nm10.pdb"
inputpdb9 = "OUTS9CCON2FBSA5nm10.pdb"
inputpdb10 = "OUTS10CCON2FBSA5nm10.pdb"
inputpdb11 = "OUTS11CCON2FBSA5nm10.pdb"
inputpdb12 = "OUTS12CCON2FBSA5nm10.pdb"
inputpdb13 = "OUTS13CCON2FBSA5nm10.pdb"
inputpdb14 = "OUTS14CCON2FBSA5nm10.pdb"
inputpdb15 = "OUTS15CCON2FBSA5nm10.pdb"
inputpdb16 = "OUTS16CCON2FBSA5nm10.pdb"
inputpdb17 = "OUTS17CCON2FBSA5nm10.pdb"
inputpdb18 = "OUTS18CCON2FBSA5nm10.pdb"
inputpdb19 = "OUTS19CCON2FBSA5nm10.pdb"
inputpdb20 = "OUTS20CCON2FBSA5nm10.pdb"
inputpdb21 = "OUTS21CCON2FBSA5nm10.pdb"
inputpdb22 = "OUTS22CCON2FBSA5nm10.pdb"
inputpdb23 = "OUTS23CCON2FBSA5nm10.pdb"
inputpdb24 = "OUTS24CCON2FBSA5nm10.pdb"
inputpdb25 = "OUTS25CCON2FBSA5nm10.pdb"
inputpdb26 = "OUTS26CCON2FBSA5nm10.pdb"
inputpdb27 = "OUTS27CCON2FBSA5nm10.pdb"
inputpdb28 = "OUTS28CCON2FBSA5nm10.pdb"
inputpdb29 = "OUTS29CCON2FBSA5nm10.pdb"
inputpdb30 = "OUTS30CCON2FBSA5nm10.pdb"
inputpdb31 = "OUTS31CCON2FBSA5nm10.pdb"
inputpdb32 = "OUTS32CCON2FBSA5nm10.pdb"
outputpdb = "COMCCON2FBSA5nm10.pdb"
input1 = open(inputpdb1, "r")
input2 = open(inputpdb2, "r")
input3 = open(inputpdb3, "r")
input4 = open(inputpdb4, "r")
input5 = open(inputpdb5, "r")
input6 = open(inputpdb6, "r")
input7 = open(inputpdb7, "r")
input8 = open(inputpdb8, "r")
input9 = open(inputpdb9, "r")
input10 = open(inputpdb10, "r")
input11 = open(inputpdb11, "r")
input12 = open(inputpdb12, "r")
input13 = open(inputpdb13, "r")
input14 = open(inputpdb14, "r")
input15 = open(inputpdb15, "r")
input16 = open(inputpdb16, "r")
input17 = open(inputpdb17, "r")
input18 = open(inputpdb18, "r")
input19 = open(inputpdb19, "r")
input20 = open(inputpdb20, "r")
input21 = open(inputpdb21, "r")
input22 = open(inputpdb22, "r")
input23 = open(inputpdb23, "r")
input24 = open(inputpdb24, "r")
input25 = open(inputpdb25, "r")
input26 = open(inputpdb26, "r")
input27 = open(inputpdb27, "r")
input28 = open(inputpdb28, "r")
input29 = open(inputpdb29, "r")
input30 = open(inputpdb30, "r")
input31 = open(inputpdb31, "r")
input32 = open(inputpdb32, "r")
fout = open(outputpdb, "w")
atoms = 0
master = []
xdim = 0
ydim = 0
zdim = 0

fout.write(title)


for line in input1:
    if line[0:4]!='ATOM':
        if line[0:3]=='TER':
            break
        print line[0:69],
        fout.write(line[0:69])
    if line[0:4]=='ATOM':
        if line[17:21] != 'DOT ':
            print line[0:69],
            fout.write(line[0:69])
        elif line[17:21] == 'DOT ':
            print line[0:69] + 'From File 1'
            fout.write(line[0:69])

for line in input2:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 2'
        fout.write(line[0:69])

for line in input3:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 3'
        fout.write(line[0:69])

for line in input4:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 4'
        fout.write(line[0:69])

for line in input5:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 5'
        fout.write(line[0:69])

for line in input6:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 6'
        fout.write(line[0:69])

for line in input7:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 7'
        fout.write(line[0:69])

for line in input8:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 8'
        fout.write(line[0:69])

for line in input9:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 9'
        fout.write(line[0:69])

for line in input10:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 10'
        fout.write(line[0:69])

for line in input11:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 11'
        fout.write(line[0:69])

for line in input12:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 12'
        fout.write(line[0:69])

for line in input13:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 13'
        fout.write(line[0:69])

for line in input14:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 14'
        fout.write(line[0:69])

for line in input15:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 15'
        fout.write(line[0:69])

for line in input16:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 16'
        fout.write(line[0:69])

for line in input17:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 17'
        fout.write(line[0:69])

for line in input18:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 18'
        fout.write(line[0:69])

for line in input19:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 19'
        fout.write(line[0:69])

for line in input20:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 20'
        fout.write(line[0:69])

for line in input21:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 21'
        fout.write(line[0:69])

for line in input22:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 22'
        fout.write(line[0:69])

for line in input23:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 23'
        fout.write(line[0:69])

for line in input24:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 24'
        fout.write(line[0:69])

for line in input25:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 25'
        fout.write(line[0:69])

for line in input26:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 26'
        fout.write(line[0:69])

for line in input27:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 27'
        fout.write(line[0:69])

for line in input28:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 28'
        fout.write(line[0:69])

for line in input29:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 29'
        fout.write(line[0:69])

for line in input30:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 30'
        fout.write(line[0:69])

for line in input31:
    if line[0:3]=='TER':
        break
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 31'
        fout.write(line[0:69])

for line in input32:
    if line[0:3]=='TER':
        print line[0:69] + 'From File 32'
        fout.write(line[0:69])
    if line[0:3]=='END':
        print line[0:69] + 'From File 32'
        fout.write(line[0:69])
    if line[17:21] == 'DOT ':
        print line[0:69] + 'From File 32'
        fout.write(line[0:69])

fout.close()

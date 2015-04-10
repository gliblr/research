import math
import datetime
import sys
from decimal import *

__author__="galibaler"
__date__ =str(datetime.datetime.now())

title = '***************************************\n      PDB 8 Way DOT File Splitter\n              version 1\n     ' + __date__ + '\n***************************************\n'
print title
inputpdb = raw_input("What is the name of the PDB file to split? ")
#inputpdb = "CDimerT1_100.pdb"
outputpdb1 = "S1" + inputpdb
outputpdb2 = "S2" + inputpdb
outputpdb3 = "S3" + inputpdb
outputpdb4 = "S4" + inputpdb
outputpdb5 = "S5" + inputpdb
outputpdb6 = "S6" + inputpdb
outputpdb7 = "S7" + inputpdb
outputpdb8 = "S8" + inputpdb
#outputpdb9 = "S9" + inputpdb
#outputpdb10 = "S10" + inputpdb
#outputpdb11 = "S11" + inputpdb
#outputpdb12 = "S12" + inputpdb
#outputpdb13 = "S13" + inputpdb
#outputpdb14 = "S14" + inputpdb
#outputpdb15 = "S15" + inputpdb
#outputpdb16 = "S16" + inputpdb
#outputpdb17 = "S17" + inputpdb
#outputpdb18 = "S18" + inputpdb
#outputpdb19 = "S19" + inputpdb
#outputpdb20 = "S20" + inputpdb
#outputpdb21 = "S21" + inputpdb
#outputpdb22 = "S22" + inputpdb
#outputpdb23 = "S23" + inputpdb
#outputpdb24 = "S24" + inputpdb
#outputpdb25 = "S25" + inputpdb
#outputpdb26 = "S26" + inputpdb
#outputpdb27 = "S27" + inputpdb
#outputpdb28 = "S28" + inputpdb
#outputpdb29 = "S29" + inputpdb
#outputpdb30 = "S30" + inputpdb
#outputpdb31 = "S31" + inputpdb
#outputpdb32 = "S32" + inputpdb
input = open(inputpdb, "r")
fout1 = open(outputpdb1, "w")
fout2 = open(outputpdb2, "w")
fout3 = open(outputpdb3, "w")
fout4 = open(outputpdb4, "w")
fout5 = open(outputpdb5, "w")
fout6 = open(outputpdb6, "w")
fout7 = open(outputpdb7, "w")
fout8 = open(outputpdb8, "w")
#fout9 = open(outputpdb9, "w")
#fout10 = open(outputpdb10, "w")
#fout11 = open(outputpdb11, "w")
#fout12 = open(outputpdb12, "w")
#fout13 = open(outputpdb13, "w")
#fout14 = open(outputpdb14, "w")
#fout15 = open(outputpdb15, "w")
#fout16 = open(outputpdb16, "w")
#fout17 = open(outputpdb17, "w")
#fout18 = open(outputpdb18, "w")
#fout19 = open(outputpdb19, "w")
#fout20 = open(outputpdb20, "w")
#fout21 = open(outputpdb21, "w")
#fout22 = open(outputpdb22, "w")
#fout23 = open(outputpdb23, "w")
#fout24 = open(outputpdb24, "w")
#fout25 = open(outputpdb25, "w")
#fout26 = open(outputpdb26, "w")
#fout27 = open(outputpdb27, "w")
#fout28 = open(outputpdb28, "w")
#fout29 = open(outputpdb29, "w")
#fout30 = open(outputpdb30, "w")
#fout31 = open(outputpdb31, "w")
#fout32 = open(outputpdb32, "w")

atoms = 0
master = []
xdim = 0
ydim = 0
zdim = 0

fout1.write(title)
fout2.write(title)
fout3.write(title)
fout4.write(title)
fout5.write(title)
fout6.write(title)
fout7.write(title)
fout8.write(title)
#fout9.write(title)
#fout10.write(title)
#fout11.write(title)
#fout12.write(title)
#fout13.write(title)
#fout14.write(title)
#fout15.write(title)
#fout16.write(title)
#fout17.write(title)
#fout18.write(title)
#fout19.write(title)
#fout20.write(title)
#fout21.write(title)
#fout22.write(title)
#fout23.write(title)
#fout24.write(title)
#fout25.write(title)
#fout26.write(title)
#fout27.write(title)
#fout28.write(title)
#fout29.write(title)
#fout30.write(title)
#fout31.write(title)
#fout32.write(title)

dotct = 4000 #number of DOT lines to place in each split file

i = 0
for line in input:
    if line[0:4]!='ATOM':
        print line[0:69],
        fout1.write(line[0:69])
        fout2.write(line[0:69])
        fout3.write(line[0:69])
        fout4.write(line[0:69])
        fout5.write(line[0:69])
        fout6.write(line[0:69])
        fout7.write(line[0:69])
        fout8.write(line[0:69])
#        fout9.write(line[0:69])
#        fout10.write(line[0:69])
#        fout11.write(line[0:69])
#        fout12.write(line[0:69])
#        fout13.write(line[0:69])
#        fout14.write(line[0:69])
#        fout15.write(line[0:69])
#        fout16.write(line[0:69])
#        fout17.write(line[0:69])
#        fout18.write(line[0:69])
#        fout19.write(line[0:69])
#        fout20.write(line[0:69])
#        fout21.write(line[0:69])
#        fout22.write(line[0:69])
#        fout23.write(line[0:69])
#        fout24.write(line[0:69])
#        fout25.write(line[0:69])
#        fout26.write(line[0:69])
#        fout27.write(line[0:69])
#        fout28.write(line[0:69])
#        fout29.write(line[0:69])
#        fout30.write(line[0:69])
#        fout31.write(line[0:69])
#        fout32.write(line[0:69])
    if line[0:4]=='ATOM':
        if line[17:21] != 'DOT ':
            print line[0:69],
            fout1.write(line[0:69])
            fout2.write(line[0:69])
            fout3.write(line[0:69])
            fout4.write(line[0:69])
            fout5.write(line[0:69])
            fout6.write(line[0:69])
            fout7.write(line[0:69])
            fout8.write(line[0:69])
#            fout9.write(line[0:69])
#            fout10.write(line[0:69])
#            fout11.write(line[0:69])
#            fout12.write(line[0:69])
#            fout13.write(line[0:69])
#            fout14.write(line[0:69])
#            fout15.write(line[0:69])
#            fout16.write(line[0:69])
#            fout17.write(line[0:69])
#            fout18.write(line[0:69])
#            fout19.write(line[0:69])
#            fout20.write(line[0:69])
#            fout21.write(line[0:69])
#            fout22.write(line[0:69])
#            fout23.write(line[0:69])
#            fout24.write(line[0:69])
#            fout25.write(line[0:69])
#            fout26.write(line[0:69])
#            fout27.write(line[0:69])
#            fout28.write(line[0:69])
#            fout29.write(line[0:69])
#            fout30.write(line[0:69])
#            fout31.write(line[0:69])
#            fout32.write(line[0:69])
        elif line[17:21] == 'DOT ':
            if i <= dotct:
                print line[0:69] + 'File 1'
                fout1.write(line[0:69])
                i = i + 1
            elif i <= dotct*2:
                print line[0:69] + 'File 2'
                fout2.write(line[0:69])
                i = i + 1
            elif i <= dotct*3:
                print line[0:69] + 'File 3'
                fout3.write(line[0:69])
                i = i + 1
            elif i <= dotct*4:
                print line[0:69] + 'File 4'
                fout4.write(line[0:69])
                i = i + 1
            elif i <= dotct*5:
                print line[0:69] + 'File 5'
                fout5.write(line[0:69])
                i = i + 1
            elif i <= dotct*6:
                print line[0:69] + 'File 6'
                fout6.write(line[0:69])
                i = i + 1
            elif i <= dotct*7:
                print line[0:69] + 'File 7'
                fout7.write(line[0:69])
                i = i + 1
            elif i <= dotct*8:
                print line[0:69] + 'File 8'
                fout8.write(line[0:69])
                i = i + 1
#            elif i <= dotct*9:
#                print line[0:69] + 'File 9'
#                fout9.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*10:
#                print line[0:69] + 'File 10'
#                fout10.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*11:
#                print line[0:69] + 'File 11'
#                fout11.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*12:
#                print line[0:69] + 'File 12'
#                fout12.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*13:
#                print line[0:69] + 'File 13'
#                fout13.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*14:
#                print line[0:69] + 'File 14'
#                fout14.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*15:
#                print line[0:69] + 'File 15'
#                fout15.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*16:
#                print line[0:69] + 'File 16'
#                fout16.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*17:
#                print line[0:69] + 'File 17'
#                fout17.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*18:
#                print line[0:69] + 'File 18'
#                fout18.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*19:
#                print line[0:69] + 'File 19'
#                fout19.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*20:
#                print line[0:69] + 'File 20'
#                fout20.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*21:
#                print line[0:69] + 'File 21'
#                fout21.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*22:
#                print line[0:69] + 'File 22'
#                fout22.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*23:
#                print line[0:69] + 'File 23'
#                fout23.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*24:
#                print line[0:69] + 'File 24'
#                fout24.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*25:
#                print line[0:69] + 'File 25'
#                fout25.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*26:
#                print line[0:69] + 'File 26'
#                fout26.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*27:
#                print line[0:69] + 'File 27'
#                fout27.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*28:
#                print line[0:69] + 'File 28'
#                fout28.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*29:
#                print line[0:69] + 'File 29'
#                fout29.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*30:
#                print line[0:69] + 'File 30'
#                fout30.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*31:
#                print line[0:69] + 'File 31'
#                fout31.write(line[0:69])
#                i = i + 1
#            elif i <= dotct*32:
#                print line[0:69] + 'File 32'
#                fout32.write(line[0:69])
#                i = i + 1

fout1.close()
fout2.close()
fout3.close()
fout4.close()
fout5.close()
fout6.close()
fout7.close()
fout8.close()
#fout9.close()
#fout10.close()
#fout11.close()
#fout12.close()
#fout13.close()
#fout14.close()
#fout15.close()
#fout16.close()
#fout17.close()
#fout18.close()
#fout19.close()
#fout20.close()
#fout21.close()
#fout22.close()
#fout23.close()
#fout24.close()
#fout25.close()
#fout26.close()
#fout27.close()
#fout28.close()
#fout29.close()
#fout30.close()
#fout31.close()
#fout32.close()

#import sys
#arg = sys.argv[1]
#print arg
#
#print '***************************************'
#print '   Solvation Free Energy Calculator'
#print '***************************************'

inputpdb = "FBSADIMERWIONTEST.pdb"
input = open(inputpdb, "r")
PDBArray = []
SASArray = []

for line in input:
    inpieces = line.split()
#    residue = inpieces[4:5]
#    iatom = inpieces[2:3]
#    hpa = inpieces[8:9]
#    inline_list = [residue, iatom, hpa]
#    print inline_list
    PDBArray.append(inpieces)

#length = 0
#for row in PDBArray:
#    length = length + 1
#print length

filename = "FBSADIMERWION"
file=open(filename,"r")
fsum=0.0

for line in file:
    pieces = line.split()
    index = pieces[0][1:line.find('@')-1]
    atom = pieces[0][line.find('@'):8]
    area = pieces[1]
    line_list = [index, atom, area]
    SASArray.append(line_list)

print 'TITLE Modified FBSADIMERWION'
print 'CRYST1  180.000  115.000  140.000  90.00  90.00  90.00 P 1'
print 'MODEL        1'

for row in PDBArray:
    residue = row[4:5]
    iatom = row[2:3]
    hpa = row[8:9]

    for sasline in SASArray:
        index = [sasline[0]]
        atom = [sasline[1]]
        area = [sasline[2]]
#    print atom, area
##    print "****************************************", index, atom, area
#    for row in PDBArray:
#        residue = row[4:5]
#        iatom = row[2:3]
#        hpa = row[8:9]
        #i = i + 1
        #print total, "/", i

        if residue == index and iatom == atom:
#            print "item found!!!!!!!!!!!!!!!!! ", residue, index, iatom, atom
#            print "starting check, atom type ", atom[0]
#            i = i + 1
#            print i
            factor = 0
            if atom[0].startswith('C'):
                factor = 16.0*float(area[0])
                fsum = fsum + factor
#                print 'Atom:', str(index[0]), str(atom[0]),' adds ', factor ,'to the sum: ', fsum, 'and was processed as C +16'
            elif atom[0].startswith('NZ') or atom[0].startswith('NH2') or atom[0].startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
                factor = -50.0*float(area[0])
                fsum = fsum + factor
#                print 'Atom:', str(index[0]),str(atom[0]),' adds ', factor , 'to the sum: ', fsum, ' and was processed as NZ or NH2 or ND1 -50'
            elif atom[0].startswith('OD2') or atom[0].startswith('OE2'):
                factor = -24.0*float(area[0])
                fsum = fsum + factor #ASP,GLU,TYR are all protonated, chrg = 0 and treated as O
#                print 'Atom:', str(index[0]), str(atom[0]),' adds ', factor , 'to the sum: ', fsum, ' and was processed as protonated OD2/OE2 -6'
            elif atom[0].startswith('O') or atom[0].startswith('N'):
                factor = -6.0*float(area[0])
                fsum = fsum + factor
#                print 'Atom:', str(index[0]), str(atom[0]),' adds ', factor , 'to the sum: ', fsum, ' and was processed as N or O -6'
            elif atom[0].startswith('S'):
                factor = 21.0*float(area[0])
                fsum = fsum + factor
#                print 'Atom:', str(index[0]), str(atom[0]),' adds ', factor , 'to the sum: ', fsum, ' and was processed as S +2'
            
            row.insert(8, factor)
            print str(row[0]), str(row[1]).rjust(6), str(row[2]).ljust(4), str(row[3]), str(row[4]).rjust(5), str(row[5]).rjust(11), str(row[6]).rjust(7), str(row[7]).rjust(7), str(row[8]).ljust(6)
#            print linebuffer
#            outputfile.writelines(linebuffer)

#outputfile.close()

print 'TER'
print 'ENDMDL'
print ''

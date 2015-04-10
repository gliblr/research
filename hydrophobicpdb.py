# To change this template, choose Tools | Templates
# and open the template in the editor.
# From Cowan R., Whittaker R.G. Peptide Research 3:75-80(1990)

__author__="galibaler"
__date__ ="$Nov 8, 2012 12:21:00 PM$"

print '***************************************'
print '      Hydrophobicity PDB Editor'
print '***************************************'


inputpdb = "BSA3.5dimerc-.pdb"
input = open(inputpdb, "r")

for line in input:
#    print line
    index = 17         #line.find('X')-4
    residue = line[17:21]
#    print index, " and ", residue
    if line[0:4]=='CRYS':
        print line[0:68]
    if residue=='ALA ':
        print line[0:62] + '0.42'
    if residue=='ARG ':
        print line[0:62] + '-1.56'
    if residue=='ASN ':
        print line[0:62] + '-1.03'
    if residue=='ASP ':
        print line[0:62] + '-0.51'
    if residue=='CYS ':
        print line[0:62] + '0.84'
    if residue=='CYSH':
        print line[0:62] + '0.84'
    if residue=='CYS2':
        print line[0:62] + '0.84'
    if residue=='GLN ':
        print line[0:62] + '-0.96'
    if residue=='GLU ':
        print line[0:62] + '-0.37'
    if residue=='GLY ':
        print line[0:62] + '0.00'
    if residue=='HIS ':
        print line[0:62] + '-2.28'
    if residue=='HISH':
        print line[0:62] + '-2.28'
    if residue=='ILE ':
        print line[0:62] + '1.81'
    if residue=='LEU ':
        print line[0:62] + '1.80'
    if residue=='LYS ':
        print line[0:62] + '-2.03'
    if residue=='LYSH':
        print line[0:62] + '-2.03'
    if residue=='MET ':
        print line[0:62] + '1.18'
    if residue=='PHE ':
        print line[0:62] + '1.74'
    if residue=='PRO ':
        print line[0:62] + '0.86'
    if residue=='SER ':
        print line[0:62] + '-0.64'
    if residue=='THR ':
        print line[0:62] + '-0.26'
    if residue=='TRP ':
        print line[0:62] + '1.46'
    if residue=='TYR ':
        print line[0:62] + '0.51'
    if residue=='VAL ':
        print line[0:62] + '1.34'
print 'END'

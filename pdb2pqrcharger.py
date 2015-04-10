__author__="galibaler"
__date__ ="$Nov 29, 2012 10:00:20 AM$"

print '***************************************'
print '        PDB2PQR Charge Editor'
print '***************************************'


inputpdb = "dimerconnelly12000OUT.pdb"
input = open(inputpdb, "r")
atomcounter = 0

for line in input:
#    print line
    index = 17         #line.find('X')-4
    residue = line[17:21]
    atom = line[12:16]
    resn = line[23:26]
#    print index, " and ", residue
    if line[0:4]!='ATOM':
        print line[0:68]
    if residue=='ALA ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB3':
            print line[0:55] + ' 0.06  1.25'            
            atomcounter = atomcounter + 1
        if atom==' C  ' and resn!='583':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ' and resn!='583':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
        if atom==' HO ' and resn=='583':
            print line[0:55] + ' 0.45  1.20'
            atomcounter = atomcounter + 1
        if atom==' OT ' and resn=='583':
            print line[0:55] + '-0.44  1.48'
            atomcounter = atomcounter + 1
        if atom==' O  ' and resn=='583':
            print line[0:55] + '-0.53  1.50'
            atomcounter = atomcounter + 1
        if atom==' C  ' and resn=='583':
            print line[0:55] + ' 0.52  1.88'
            atomcounter = atomcounter + 1
    if residue=='ARG ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.05  1.75'            
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HG2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD ':
            print line[0:55] + ' 0.19  1.75'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' NE ':
            print line[0:55] + '-0.70  1.62'
            atomcounter = atomcounter + 1
        if atom==' HE ':
            print line[0:55] + ' 0.44  1.20'
            atomcounter = atomcounter + 1
        if atom==' CZ ':
            print line[0:55] + ' 0.64  1.12'
            atomcounter = atomcounter + 1
        if atom==' NH1':
            print line[0:55] + '-0.80  1.62'
            atomcounter = atomcounter + 1
        if atom=='HH11':
            print line[0:55] + ' 0.46  1.20'
            atomcounter = atomcounter + 1
        if atom=='HH12':
            print line[0:55] + ' 0.46  1.20'
            atomcounter = atomcounter + 1
        if atom==' NH2':
            print line[0:55] + '-0.80  1.62'
            atomcounter = atomcounter + 1
        if atom=='HH21':
            print line[0:55] + ' 0.46  1.20'
            atomcounter = atomcounter + 1
        if atom=='HH22':
            print line[0:55] + ' 0.46  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='ASN ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + ' 0.50  1.88'            
            atomcounter = atomcounter + 1
        if atom==' OD1':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
        if atom==' ND2':
            print line[0:55] + '-0.76  1.62'
            atomcounter = atomcounter + 1
        if atom=='HD21':
            print line[0:55] + ' 0.38  1.20'
            atomcounter = atomcounter + 1
        if atom=='HD22':
            print line[0:55] + ' 0.38  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='ASP ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' H1 ':
            print line[0:55] + ' 0.33  1.20'
            atomcounter = atomcounter + 1
        if atom==' H2 ':
            print line[0:55] + ' 0.33  1.20'
            atomcounter = atomcounter + 1
        if atom==' H3 ':
            print line[0:55] + ' 0.33  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + ' 0.52  1.88'            
            atomcounter = atomcounter + 1
        if atom==' OD1':
            print line[0:55] + '-0.53  1.48'
            atomcounter = atomcounter + 1
        if atom==' OD1':
            print line[0:55] + '-0.44  1.50'
            atomcounter = atomcounter + 1            
        if atom==' HD2':
            print line[0:55] + ' 0.45  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='CYS ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + ' 0.10  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' SG ' and resn==' 34':
            print line[0:55] + '-0.34  1.80'
            atomcounter = atomcounter + 1
        if atom==' SG ' and resn!=' 34':
            print line[0:55] + '-0.22  1.77'
            atomcounter = atomcounter + 1
        if atom==' HG ':
            print line[0:55] + ' 0.16  1.20'            
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='GLN ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HG2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' OE1':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
        if atom==' NE2':
            print line[0:55] + '-0.76  1.62'
            atomcounter = atomcounter + 1
        if atom=='HE21':
            print line[0:55] + ' 0.38  1.20'
            atomcounter = atomcounter + 1
        if atom=='HE22':
            print line[0:55] + ' 0.38  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='GLU ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.12  1.75'            
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HG2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD ':
            print line[0:55] + ' 0.52  1.88'
            atomcounter = atomcounter + 1
        if atom==' OE1':
            print line[0:55] + '-0.44  1.48'
            atomcounter = atomcounter + 1
        if atom==' OE2':
            print line[0:55] + '-0.53  1.50'
            atomcounter = atomcounter + 1
        if atom==' HE2':
            print line[0:55] + ' 0.45  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='GLY ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.08  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HA2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='HIS ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.00  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + ' 0.22  1.77'
            atomcounter = atomcounter + 1
        if atom==' ND1':
            print line[0:55] + '-0.54  1.62'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.46  1.20'
            atomcounter = atomcounter + 1
        if atom==' CD2':
            print line[0:55] + ' 0.22  1.77'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CE1':
            print line[0:55] + ' 0.38  1.77'
            atomcounter = atomcounter + 1
        if atom==' HE1':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' NE2':
            print line[0:55] + '-0.54  1.62'
            atomcounter = atomcounter + 1
        if atom==' HE2':
            print line[0:55] + ' 0.46  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='ILE ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.06  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG1':
            print line[0:55] + '-0.12  1.75'            
            atomcounter = atomcounter + 1
        if atom=='HG11':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG12':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG2':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom=='HG21':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG22':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG23':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD ':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HD3':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='LEU ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.06  1.75'
            atomcounter = atomcounter + 1
        if atom==' HG ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD1':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom=='HD11':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HD12':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HD13':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD2':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom=='HD21':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HD22':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HD23':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='LYS ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HG2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CE ':
            print line[0:55] + ' 0.19  1.75'
            atomcounter = atomcounter + 1
        if atom==' HE1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HE2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' NZ ':
            print line[0:55] + '-0.30  1.62'
            atomcounter = atomcounter + 1
        if atom==' HZ1':
            print line[0:55] + ' 0.33  1.20'
            atomcounter = atomcounter + 1
        if atom==' HZ2':
            print line[0:55] + ' 0.33  1.20'
            atomcounter = atomcounter + 1
        if atom==' HZ3':
            print line[0:55] + ' 0.33  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='MET ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + ' 0.05  1.75'
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HG2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' SD ':
            print line[0:55] + '-0.34  1.80'
            atomcounter = atomcounter + 1
        if atom==' CE ':
            print line[0:55] + '-0.01  1.75'
            atomcounter = atomcounter + 1
        if atom==' HE1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HE2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HE3':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='PHE ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.00  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' CD1':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CD2':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CE1':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HE1':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CE2':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HE2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CZ ':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HZ ':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='PRO ':
        if atom==' N  ':
            print line[0:55] + '-0.14  1.62'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.01  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HG2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CD ':
            print line[0:55] + '-0.05  1.75'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='SER ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' OG ':
            print line[0:55] + '-0.68  1.56'
            atomcounter = atomcounter + 1
        if atom==' HG ':
            print line[0:55] + ' 0.42  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='THR ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + ' 0.20  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' OG1':
            print line[0:55] + '-0.68  1.56'
            atomcounter = atomcounter + 1
        if atom==' HG1':
            print line[0:55] + ' 0.42  1.20'
            atomcounter = atomcounter + 1
        if atom==' CG2':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom=='HG21':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG22':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG23':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='TRP ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.12  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + ' 0.08  1.77'
            atomcounter = atomcounter + 1
        if atom==' CD1':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CD2':
            print line[0:55] + '-0.05  1.77'
            atomcounter = atomcounter + 1
        if atom==' NE1':
            print line[0:55] + '-0.57  1.62'
            atomcounter = atomcounter + 1
        if atom==' HE1':
            print line[0:55] + ' 0.42  1.20'
            atomcounter = atomcounter + 1
        if atom==' CE2':
            print line[0:55] + ' 0.13  1.77'
            atomcounter = atomcounter + 1
        if atom==' CE3':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HE3':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CZ2':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HZ2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CZ3':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HZ3':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CH2':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HH2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='TYR ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.00  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB1':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' HB2':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG ':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' CD1':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HD1':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CD2':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HD2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CE1':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HE1':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CE2':
            print line[0:55] + '-0.12  1.77'
            atomcounter = atomcounter + 1
        if atom==' HE2':
            print line[0:55] + ' 0.12  1.21'
            atomcounter = atomcounter + 1
        if atom==' CZ ':
            print line[0:55] + ' 0.15  1.77'
            atomcounter = atomcounter + 1
        if atom==' OH ':
            print line[0:55] + '-0.58  1.54'
            atomcounter = atomcounter + 1
        if atom==' HH ':
            print line[0:55] + ' 0.44  1.20'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='VAL ':
        if atom==' N  ':
            print line[0:55] + '-0.50  1.62'
            atomcounter = atomcounter + 1
        if atom==' H  ':
            print line[0:55] + ' 0.30  1.20'
            atomcounter = atomcounter + 1
        if atom==' CA ':
            print line[0:55] + ' 0.14  1.75'
            atomcounter = atomcounter + 1
        if atom==' HA ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CB ':
            print line[0:55] + '-0.06  1.75'
            atomcounter = atomcounter + 1
        if atom==' HB ':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG1':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom=='HG11':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG12':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG13':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' CG2':
            print line[0:55] + '-0.18  1.75'
            atomcounter = atomcounter + 1
        if atom=='HG21':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG22':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom=='HG23':
            print line[0:55] + ' 0.06  1.25'
            atomcounter = atomcounter + 1
        if atom==' C  ':
            print line[0:55] + ' 0.50  1.88'
            atomcounter = atomcounter + 1
        if atom==' O  ':
            print line[0:55] + '-0.50  1.48'
            atomcounter = atomcounter + 1
    if residue=='SOL ':
        if atom==' OW ':
            print line[0:55] + '-0.82  1.58'
            atomcounter = atomcounter + 1
        if atom==' HW1':
            print line[0:55] + ' 0.41  1.20'
            atomcounter = atomcounter + 1
        if atom==' HW2':
            print line[0:55] + ' 0.41  1.20'
            atomcounter = atomcounter + 1
    if residue=='CL- ':
        if atom==' CL ':
            print line[0:55] + '-1.00  2.21'
            atomcounter = atomcounter + 1
    if residue=='DOT ':
        print line[0:55] + ' 0.00  0.00'

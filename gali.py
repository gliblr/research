#import sys
#arg = sys.argv[1]
#print arg

print '***************************************'
print '   Solvation Free Energy Calculator'
print '***************************************'

filename = "FBSASAS"
file=open(filename,"r")

fsum=0.0

for line in file:
    pieces = line.split()
    index = pieces[0][1:line.find('@')-1]
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        fsum = fsum + 16.0*float(pieces[1])
        print 'Atom:', index, atom,' adds ',16*float(pieces[1]) ,'to the sum: ', fsum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        fsum = fsum - 50.0*float(pieces[1])
        print 'Atom:', index, atom,' adds ',-50*float(pieces[1]), 'to the sum: ', fsum, ' and was processed as NZ or NH2 or ND1 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        fsum = fsum - 6.0*float(pieces[1]) #ASP,GLU,TYR are all protonated, chrg = 0 and treated as O                             
        print 'Atom:', index, atom,' adds ',-6*float(pieces[1]), 'to the sum: ', fsum, ' and was processed as protonated OD2/OE2 -6'
    elif atom.startswith('O') or atom.startswith('N'):
        fsum = fsum - 6.0*float(pieces[1])
        print 'Atom:', index, atom,' adds ',-6*float(pieces[1]), 'to the sum: ', fsum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        fsum = fsum + 21.0*float(pieces[1])
        print 'Atom:', index, atom,' adds ',21*float(pieces[1]), 'to the sum: ', fsum, ' and was processed as S +21'


filename = "FBSADIMER"
file=open(filename,"r")

fdimsum=0.0

for line in file:
    pieces = line.split()
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        fdimsum = fdimsum + 16.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',16*float(pieces[1]) ,'to the sum: ', nsum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        fdimsum = fdimsum - 50.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-50*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as NZ or NH2 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        fdimsum = fdimsum - 6.0*float(pieces[1]) #ASP, GLU are all unprotonated, chrg = -1, TYR protonated chrg = 0
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as OD2/OE2 -6'
    elif atom.startswith('O') or atom.startswith('N'):
        fdimsum = fdimsum - 6.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        fdimsum = fdimsum + 21.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',21*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as S +21'


filename = "FBSADIMERNION"
file=open(filename,"r")

fdimnionsum=0.0

for line in file:
    pieces = line.split()
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        fdimnionsum = fdimnionsum + 16.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',16*float(pieces[1]) ,'to the sum: ', nsum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        fdimnionsum = fdimnionsum - 50.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-50*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as NZ or NH2 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        fdimnionsum = fdimnionsum - 6.0*float(pieces[1]) #ASP, GLU are all unprotonated, chrg = -1, TYR protonated chrg = 0
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as OD2/OE2 -6'
    elif atom.startswith('O') or atom.startswith('N'):
        fdimnionsum = fdimnionsum - 6.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        fdimnionsum = fdimnionsum + 21.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',21*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as S +21'

filename = "FBSADIMERWION"
file=open(filename,"r")

fdimwionsum=0.0

for line in file:
    pieces = line.split()
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        fdimwionsum = fdimwionsum + 16.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',16*float(pieces[1]) ,'to the sum: ', nsum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        fdimwionsum = fdimwionsum - 50.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-50*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as NZ or NH2 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        fdimwionsum = fdimwionsum - 6.0*float(pieces[1]) #ASP, GLU are all unprotonated, chrg = -1, TYR protonated chrg = 0
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as OD2/OE2 -6'
    elif atom.startswith('O') or atom.startswith('N'):
        fdimwionsum = fdimwionsum - 6.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        fdimwionsum = fdimwionsum + 21.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',21*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as S +21'

filename = "FBSASASeq"
file=open(filename,"r")

feqnsum=0.0

for line in file:
    pieces = line.split()
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        feqnsum = feqnsum + 16.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',16*float(pieces[1]) ,'to the sum: ', nsum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        feqnsum = feqnsum - 50.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-50*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as NZ or NH2 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        feqnsum = feqnsum - 6.0*float(pieces[1]) #ASP, GLU are all unprotonated, chrg = -1, TYR protonated chrg = 0
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as OD2/OE2 -6'
    elif atom.startswith('O') or atom.startswith('N'):
        feqnsum = feqnsum - 6.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        feqnsum = feqnsum + 21.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',21*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as S +21'


filename = "NBSASAS"
file=open(filename,"r")

nsum=0.0

for line in file:
    pieces = line.split()
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        nsum = nsum + 16.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',16*float(pieces[1]) ,'to the sum: ', nsum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        nsum = nsum - 50.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-50*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as NZ or NH2 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        nsum = nsum - 6.0*float(pieces[1]) #ASP, GLU are all unprotonated, chrg = -1, TYR protonated chrg = 0
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as OD2/OE2 -6'
    elif atom.startswith('O') or atom.startswith('N'):
        nsum = nsum - 6.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        nsum = nsum + 21.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',21*float(pieces[1]), 'to the sum: ', nsum, ' and was processed as S +21'

filename = "UBSASAS"
file=open(filename,"r")

usum=0.0

for line in file:
    pieces = line.split()
    atom = pieces[0][line.find('@'):8]
    if atom.startswith('C'):
        usum = usum + 16.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',16*float(pieces[1]) ,'to the sum: ', usum, 'and was processed as C +16'
    elif atom.startswith('NZ') or atom.startswith('NH2') or atom.startswith('ND1'): #LYS,ARG,HIS protonated chrg = 1
        usum = usum - 50.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-50*float(pieces[1]), 'to the sum: ', usum, ' and was processed as NZ or NH2 -50'
    elif atom.startswith('OD2') or atom.startswith('OE2'):
        usum = usum - 6.0*float(pieces[1]) #ASP, GLU are all unprotonated, chrg = -1, TYR protonated chrg = 0
#        print 'Atom:', atom,' adds ',-24*float(pieces[1]), 'to the sum: ', usum, ' and was processed as OD2/OE2 -24'
    elif atom.startswith('O') or atom.startswith('N'):
        usum = usum - 6.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',-6*float(pieces[1]), 'to the sum: ', usum, ' and was processed as N or O -6'
    elif atom.startswith('S'):
        usum = usum + 21.0*float(pieces[1])
#        print 'Atom:', atom,' adds ',21*float(pieces[1]), 'to the sum: ', usum, ' and was processed as S +21' 

print 'Calculation Summary'
delFBSA = (fsum-usum)/1000
delNBSA = (nsum-usum)/1000
delFBSADIM = (fdimsum-usum)/1000
delFBSADIMNION = (fdimnionsum-usum)/1000
delFBSADIMWION = (fdimwionsum-usum)/1000
delFeqBSA = (feqnsum-usum)/1000
print 'Reference UBSA Conformation Solvation Energy: ', usum/1000, ' kcal/mol'
print 'FBSA Change in Conformation Solvation Energy: ', delFBSA, ' kcal/mol'
print 'FBSAeq Change in Conformation Solvation Energy: ', delFeqBSA, ' kcal/mol'
print 'FBSADIM Change in Conformation Solvation Energy:', delFBSADIM, 'kcal/mol'
print 'FBSADIMNION Change in Conformation Solvation Energy:', delFBSADIMNION, 'kcal/mol'
print 'FBSADIMWION Change in Conformation Solvation Energy:', delFBSADIMWION, 'kcal/mol'
print 'NBSA Change in Conformation Solvation Energy: ', delNBSA, ' kcal/mol'
print 'Difference in Solvation Free Energy FBSA-NBSA: ', delFBSA-delNBSA, ' kcal/mol'
print 'Difference in Solvation Free Energy: FBSAeq-NBSA', delFeqBSA-delNBSA, ' kcal/mol'
print 'Difference in Solvation Free Energy FBSADIM-FBSADIMNION: ', delFBSADIM-delFBSADIMNION, ' kcal/mol'
print 'Difference in Solvation Free Energy FBSADIM-FBSADIMWION: ', delFBSADIM-delFBSADIMWION, ' kcal/mol'
print 'Difference in Solvation Free Energy FBSADIMWION-FBSADIMNION: ', delFBSADIMWION-delFBSADIMNION, ' kcal/mol'
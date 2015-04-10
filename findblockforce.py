#usr/bin/env/python
import sys
#import sys,numpy,math,random
#from math import pow,log,pow,acos
#avgforce=open(sys.argv[2],'a')
splitforce=open(sys.argv[2],'w')
flist=open(sys.argv[1],'r').readlines()
temp=open("temp",'w')
length=len(flist)
start=23
step=1000000
nsteps=10
a=[0]*nsteps
sumt=0.0
t=start
n=0
c=0
while n<nsteps:
        t=start+step*n
        while t<start+step*(n+1):
                ti= flist[t].split()
                a[n]+=float(ti[1])
                sumt+=float(ti[1])
                c+=1
                t+=1
        print >> splitforce,a[n]/step/10/2.5
	sumt+=a[n]
        n+=1

print c
print >> splitforce, sumt/(step*nsteps)/10/2.5

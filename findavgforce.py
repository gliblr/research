#/usr/bin/env/python

inp=open("INPUT",'r').readlines()
out=open("OUTPUT",'a')
L=len(inp)
avg=0
S=L-2000000
for i in range(S,L):
	avg=avg+float(inp[i].split()[1])
avg=avg/2000000        #(S)/10/2.78
print >> out,avg

#/usr/bin/env/python

import sys, math
inp=open('INPUT','r').readlines()
#inp2=open('INPU2','r').readlines()
#inp3=open('INPU3','r').readlines()
out=open('OUTPUT','a')
L=len(inp)
#L2=len(inp2)
#L3=len(inp3)
n=NUM
x=1000000
#print '***',n,'***'
d = int((L-math.fmod(L,x))/x)
#d2 = int((L2-math.fmod(L2,x))/x)
#d3 = int((L3-math.fmod(L3,x))/x)
D = d
#print 'D=',D
s=[0]*D
for i in range(0,d):
    for j in range(0,x):
         k = L-(i+1)*x+j
         s[i]+=float(inp[k].split()[1])
          
tot=s
avg=tot/(d)
sum=0
for i in range(0,D):
    sum += pow(s[i]-avg,2)
std=math.sqrt(sum/D)       

print >>out, avg,std


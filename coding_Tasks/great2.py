n=int(input())
numb=raw_input()
lis=list(map(int,numb.split()))
big,sbig,ssbig=-6000,-6000,-6000
for i in lis:
	if(i>big):
		big,sbig,ssbig=i,big,sbig

print big,sbig,ssbig

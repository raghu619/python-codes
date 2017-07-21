
import re
#k=[]
#arr=[[a,b,c,d]  for a in s for b in s for c in s if (s[a]==s[d] and s[b]==s[c]) ]
#for i in range(len(s)):
 #    if(s[i]==s[i+2]  and s[i+1]==s[i+2]):
          #print "true" """for j in range(3):
           # k.append(s[j])"""    
#print k
p=input("Enter the string\n")
k=bool(re.search(r"(\w)\1+(\w)",p))
print(k)


"""s=int(raw_input().split())
for i in range(len(s)):

	for j in range(i)"""

"""s=[]
n=int(raw_input())
for i in range(n):

  s.append(raw_input())

s.sort()
l=[]
l=set(s)

print(l[n-2])  

n = int(input())
numb = input()
lis = list(map(int, numb.split()))
big, sbig = -6000, -6000
for i in lis:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)
"""
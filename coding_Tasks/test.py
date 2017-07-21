n=raw_input()

k=[]
s=[]
count=0
for i in range(0,len(n),3):
  

  s=[ n[j]   for j in range(i,(i+3)) ] 
  

  k.append(s)
         

print k      



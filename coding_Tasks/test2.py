l=[]
from collections  import Counter
for k in  range(int(raw_input())):
     l.append(str(raw_input()))

  
cnt=Counter()
for x in l:
   cnt[x]+=1


print cnt             
 
                

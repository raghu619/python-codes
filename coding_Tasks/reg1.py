
#for i in range(int(raw_input())):
 #   print bool(re.search(r"^[+-]?\d*\.\d+$",raw_input().strip()))
#p=raw_input()
#r=(re.search(r"^([_+<-])?(\d)\d\d*",p))
#print(r.group(0))
#print(r.group(1))
#print(r.group(2))

import re
m = re.search(r'\d?(\d)\d+',raw_input())
#if m:
print m.group(0)
print m.group(1)
#else:
    #print -1
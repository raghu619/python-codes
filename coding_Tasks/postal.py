import sys
postal=int(sys.stdin.readline())
code=[int(d) for d in str(postal)]
for i in code:
  if(i==i+2):
   print("such") 



print(code)
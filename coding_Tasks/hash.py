
n=int(raw_input())
s=[]

for i in range(n):
  s.append(int(raw_input()))


m=tuple(s)

print m[0],m[1]
print (hash((m)))


#list1=map(list,s)
#print list1
#print (hash((t))

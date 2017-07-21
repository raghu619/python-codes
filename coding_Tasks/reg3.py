import re
p=raw_input()
k=raw_input("")
m=(re.finditer(r"("+k+")+",p))
anymatch="no"
for k in m:
	anymatch="yes"
	print ((k.start(),k.end()-1))
if anymatch=="no":
  print((-1,-1))
#print (""+str(m.start())+","+str(m.end())+"")


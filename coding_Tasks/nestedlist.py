k=[]
low,slow=6000,6000
bigname,sbigname="",""
n=int(raw_input())
if(n!=3):
    for i in range(n):
      name = raw_input()
      score = float(raw_input())
      k.append([name,score])
        
    for x,y in k:
      if(y<low):
        low,slow=y,low
        bigname,sbigname=x,bigname
      elif(y>low and y<slow):
            slow=y
            sbigname,bigname=x,sbigname 
 m=0  
 rm,km="",""
 for x,y in k:
  if(y==slow):
    rm,km=x,rm
    m=m+1 

 if(m==2):
 print rm 
 print km
 else:
  print sbigname 
import re
value=raw_input()
result=re.sub(r"\w+[a-zA-Z]+\w*$",r"\w+[A-Za-z]+\w$",value)
print result

string.swapcase(s) 
k=line.split(" ")
    k="-".join(k)
    return k




    def mutate_string(string, position, character):
       string=string[:position]+character+string[(position+1):]
       return string
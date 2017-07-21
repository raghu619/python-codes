import re

#k=re.findall(r"\w+[aeiou][aeiou]*\w+",p)
#print k
#consonants = 'qwrtypsdfghjklzxcvbnm'
#vowels = 'aeiou'
#match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',raw_input(),flags = re.I)
#if match:
   # for i in match:
  #      print i
#else:
 #   print -1
p=raw_input()
k=re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])",p)
#m=re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])([aieou]{2,})(?=)*",p)
print k
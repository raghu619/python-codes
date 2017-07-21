import re

def count_substring(string, sub_string):
     
    k=re.findall(r"?="+sub_string+"",string)


    print k



count_substring(raw_input(),raw_input())    

nums = [1, 2, -1, 9, -5]
genexp = (x > 0 for x in nums)
 for x in genexp:
        print x


 print any([x.isalnum() for x in s])
    print any([x.isalpha() for x in s])
    print any([x.isdigit() for x in s])
    print any([x.islower() for x in s])
    print any([x.isupper() for x in s])
    
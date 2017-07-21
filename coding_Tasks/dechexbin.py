#def print_formatted(number):
    # your code goes here
 #   for i in range(1,number):
  #      print(tohex(i))

#print_formatted(6)   
def fun(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)

n = input()
fun(n)     
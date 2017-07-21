def gen(N):
	for i in range(N):
		yield i


k=gen(3)
print k.next()



M = raw_input();m = raw_input().split()
N = raw_input();n = raw_input().split()

print "\n".join(sorted(list(set(m) ^ set(n)),key=int))
	
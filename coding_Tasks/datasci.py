n = int(raw_input())
s = set([int(x) for x in raw_input().strip().split()]) 
for _ in range(int(raw_input())):

    a = list(raw_input().strip().split())

    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print sum(s)    

a = int(raw_input())
A = set(map(int, raw_input().split()))
for i in range(int(raw_input())):
    s, b = raw_input().split()
    if s == 'intersection_update':
        A &= set(map(int, raw_input().split()))
    elif s == 'update':
        A |= set(map(int, raw_input().split()))
    elif s == 'symmetric_difference_update':
        A ^= set(map(int, raw_input().split()))
    else:
        A -= set(map(int, raw_input().split()))
print sum(A)  
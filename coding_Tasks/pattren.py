
n = int(raw_input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

    S = raw_input().strip()
S_length = len(S)
player1, player2 = 0,0

for i in xrange(S_length):
    if S[i] in "AEIOU":
        player1 += S_length - i
    else:
        player2 += S_length - i        
        
if player1 > player2:
    print "Kevin", player1
elif player1 < player2:
    print "Stuart", player2
else:
    print "Draw"
B
BA
BAN
BANA
BANAN
BANANA
A
AN
ANA
ANAN
ANANA
N
NA
NAN
NANA
A
AN
ANA
N
NA
A
It is interesting to note that in BANANA:
Words formed using the first letter B       = 6
Words formed using the second letter A  = 5
Words formed using the third letter N     = 4
Words formed using the fourth letter A    = 3
Words formed using the fifth letter N      = 2
Words formed using the last letter A       = 1
Using this pattern, you can run a loop from the start to the end of the string and filter out words starting with vowels and consonants.
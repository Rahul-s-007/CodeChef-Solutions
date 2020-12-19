n = int(input())
for i in range(n):
    s = input()
    l = len(s)
    if (l%2) == 0:
        s1 = s[:(l//2)]
        s2 = s [(l//2):]
    else:
        s1 = s[:(l//2)]
        s2 = s [((l//2)+1):]
    
    ss1 = [str(i) for i in s1]
    ss1.sort()
    ss2 = [str(i) for i in s2]
    ss2.sort()
    
    if ss1 == ss2:
        print("YES")
    else: print("NO")

"""
Test case:

6
gaga
abcde
rotor
xyzxy
abbaab
ababc
"""
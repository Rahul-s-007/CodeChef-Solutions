"""
https://www.codechef.com/IARCSJUD/problems/GREATESC

Question:
The first line of the input contains two integers N and M

N  is the number of buildings. buildings are numbered 1,2,...,N

M  is the number of pairs of buildings that the director lists as being close enough to jump from one to the other

Each of the next M lines, lines 2,...,M+1, contains a pair of integers representing a pair of buildings that are close

#Line i+1 contains integers Ai and Bi, 1≤Ai≤N and 1≤Bi≤N, indicating that buildings Ai and Bi are close enough

The last line, line M+2 contains a pair of integers S and T, where S is the building from which the Hero starts his search and T is the building where the captive is held.
"""

"""
Test cases:
#1 Output: 3
Input:
5 5
1 3
2 3
1 2
3 5
4 5
1 4

#2 Output: 0
Input:
5 3
1 3
1 2
4 5
1 4

# Seprator print("--------------------")
"""

#Algo
#* We are subtracting 1 from coordinates values as buildings start from 1 but lists start from 0

#Take values of N and M
s=[int(i) for i in input().split()]
n=s[0]
m=s[1]

#Create empty board of order N*N
a=[[0 for _ in range(n)] for _ in range(n)]
print("--------------------")

while m>0:
    #Take pair of buildings closest to each other
    s=[int(i) for i in input().split()]
    print(s)
    print("--------------------")
    i=s[0]-1
    j=s[1]-1
    print("i=",i,"- j=",j)
    print("--------------------")

    a[i][j]=1
    a[j][i]=1

    #Decrement value of m" as we take the M pairs of inputs
    m-=1

# Take input of Start and End Locations
s=[int(i) for i in input().split()]
source = s[0]-1
dest = s[1]-1

# To check for already visited buildings
v = [0 for i in range(n)]

# To see steps required to reach a building
g = [0 for i in range(n)]

q = [source]
v[source]=1

para = 0
print("Part--------------------")

while True:
    u=q[para]
    print(u)
    print("--------------------")
    for i in range(n):
        # Check not visited and closest
        if a[u][i]==1 and v[i]==0:
            #Steps taken to reach that particular building
            g[i]=g[u]+1
            # Mark building visited
            v[i]=1
            q.append(i)
    if para == len(q)-1:
        break
    else:
        para += 1

print(g[dest])


"""
This pure code without any comments or unnecessary print statements

s=[int(i) for i in input().split()]
n=s[0]
m=s[1]

a=[[0 for _ in range(n)] for _ in range(n)]

while m>0:
    s=[int(i) for i in input().split()]
    i=s[0]-1
    j=s[1]-1

    a[i][j]=1
    a[j][i]=1

    m-=1

s=[int(i) for i in input().split()]
src=s[0]-1
dest=s[1]-1

v=[0 for i in range(n)]
d=[0 for i in range(n)]
q=[src]
v[src]=1
f=0

while True:
    u=q[f]
    for i in range(n):
        if a[u][i]==1 and v[i]==0:
            d[i]=d[u]+1
            v[i]=1
            q.append(i)
    if f==len(q)-1:
        break
    else:
        f+=1

print(d[dest])
"""
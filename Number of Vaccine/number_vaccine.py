a = [int(i) for i in input().split()]
#print(a)

# D1 , V1, D2, V2 and P

d1 = a[0]
v1 = a[1]
d2 = a[2]
v2 = a[3]
p = a[4]

vac = 0

day = min(d1,d2)-1
#print(day)

# This stores how many vaccines produced on each day
vac_day = [0]*day

def equal():
    global day,vac,p,v1,v2
    while vac < p:
        day += 1
        vac += (v1 + v2)
        vac_day.append(v1+v2)

def unequal(dif,v):
    global day,vac,p
    c = 0
    while vac < p:
        c = c+1
        day = day + 1
        vac = vac + v
        vac_day.append(v)
        if c == dif: break
    equal()

if d1 == d2:
    equal()

if d1 < d2:
    diff = d2 - d1
    unequal(diff,v1)

if d2 < d1:
    diff = d1 - d2
    unequal(diff,v2)

print(day)
print(vac_day)

#5 4 2 10 100 ans- 9
# 3 4 3 5 22 ans- 3
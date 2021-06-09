from numpy import *
a1=array([
    [12,13,45],
    [13,16,14],
    [1,2,3]
])
m1=matrix(a1)
print(m1)
a2=array([
    [1,2,3],
    [1,3,4],
    [2,4,3]

])
m2=matrix(a2)
print(m2)
m3=m1*m2
print(m3)
a3=array([[0,0,0],[0,0,0], [0,0,0]])
m3=matrix(a3)
for i in range(3):
    for j in range(3):
        for x in range(3):
            m3[i,j]+=m1[i,x]*m2[x,i]

print(a3)

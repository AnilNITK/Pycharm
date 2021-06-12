from array import *
a=array('i',[1,25,12,43,23,])
i=0
while i<len(a):
    j=0
    while j<i:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    i+=1
print(a)

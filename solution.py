import sys


xy = input().split(' ')
xy=int(xy[0])
#print(x)


def mer(a):
    min1=a[0]
    max1= a[0]
    for QQ in a:
        if QQ > max1:
            max1 = QQ
        if QQ< min1:
            min1 = QQ
    
    med = (min1+max1)//2
    The_ele= a[1]
    temp = abs(med-The_ele)
    a=a[1:len(a)-1]
    for tt in a :
        if abs(med-tt)<temp:
            The_ele=tt
            temp = abs(med-tt)
        
    return (max1-min1)+(max1-The_ele)+(The_ele-min1)
    


def new_para():
    x = input().split(' ')
    x=int(x[0])
    b=input().split(' ')
    c=[0]*x
    for i in range(x):
        c[i]=int(b[i])
    print(mer(c))
    return
    ##yaha c jo h vhi h apna array 
    
    
for ijk in range(xy):
    new_para()
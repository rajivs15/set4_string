n=int(input())
a=0
b=1
print(b, end=" ")
for i in range (0,n-1):
    
    c=a+b
    a=b
    b=c
    print(c, end=" ")

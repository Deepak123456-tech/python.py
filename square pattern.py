'''n=4
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()



n=4
for i in range(n):
    for j in range(n):
        if j<i+1:
            print(j+1,end="")
        else:
            print("",end="")
    print()
    
n=4
for i in range(n):
    for j in range(n):
        if j<i:
            print("",end="")
        else:
            print(j+1,end="")
    print()       


n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
n=4
for i in range(n-1,-1,-1):
    for j in range(n):
        if i==n or j==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

    
n=5
for i in range(2*n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    





























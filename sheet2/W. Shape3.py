n = int(input())

for i in range(1,n+1):
    for j in range(i,n):
        print(end=" ")
    for k in range(i*2-1):
        print("*",end="")
    print(end="\n")

for i in range(n-1,-1,-1):
    for j in range(i,n-1):
        print(end=" ")
    for k in range(i*2+1):
        print("*",end="")
    print(end="\n")


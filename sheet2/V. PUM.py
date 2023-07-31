n = int(input())
s = 1
k = 3
for i in range(n):
    for j in range(s,k+1):
        print(j,end=" ")
    print("PUM")
    s = k + 2
    k += 4


n = int(input())

for i in range(n):
    t = input()
    for j in t[::-1]:
        print(j,end=" ")
    print(end="\n")
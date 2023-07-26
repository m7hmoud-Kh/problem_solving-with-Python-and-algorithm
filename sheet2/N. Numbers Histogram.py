s = input()
x = int(input())
n = list(map(int,input().split()))
for i in n:
    for _ in range(i):
        print(s,end="")
    print(sep="\n")
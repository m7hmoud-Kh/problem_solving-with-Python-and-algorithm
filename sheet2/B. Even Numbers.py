a = int(input())
flag = 1
for i in range(1,a+1):
    if i % 2 == 0:
        print(i)
        flag = 0
if flag:
    print(-1)

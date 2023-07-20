l1, r1, l2, r2 = map(int, input().split())

if l2 >= l1 and r2 <= r1:
    print(l2, r2)
elif l1 >= l2 and r1 >= r2 and r2 >= l1:
    print(l1,r2)
elif r1 >= l2 and r1 <= r2 and l2 >= l1:
    print(l2,r1)
elif l1 >= l2 and r2 >= r1:
    print(l1,r1)

else:
    print(-1)
n = list(input())
copy_n = n.copy()
n.reverse()
if copy_n == n:
    print(''.join(n))
    print("YES")
else:
    print(int(''.join(n)))
    print("NO")


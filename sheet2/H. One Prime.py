n = int(input())

prime = False
if n > 2:
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
        else:
            prime = True
elif n == 2:
    prime = True
if prime:
    print("YES")
else:
    print("NO")
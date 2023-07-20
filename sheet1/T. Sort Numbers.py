a, b, c = map(int, input().split())

min_number = min(a,b,c)
if a == min_number:
    print(a)
    if b <= c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b == min_number:
    print(b)
    if a <= c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
elif c == min_number:
    print(c)
    if b <= a:
        print(b)
        print(a)
    else:
        print(a)
        print(b)
print(sep="\n")
print(a,b,c,sep="\n")
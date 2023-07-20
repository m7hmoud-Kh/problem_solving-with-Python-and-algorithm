a, s, b, q, c = input().split()
a, b, c = map(int, [a, b, c])

if s == "+":
    result = "Yes" if (a + b == c) else a+b
elif s == "-":
    result = "Yes" if (a - b == c) else a-b
else:
    result = "Yes" if (a * b == c) else a*b

print(result)
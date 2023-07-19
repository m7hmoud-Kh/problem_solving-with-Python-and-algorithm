import re
a = input()
a, s, b =  re.split(r'([*+/-])', a)
a,b = map(int,[a,b])
if s == "+":
    print(a+b)
elif s == "-":
    print(a-b)
elif s == "*":
    print(a*b)
else:
    print(int(a/b))
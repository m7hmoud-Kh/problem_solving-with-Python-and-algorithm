a, s, b = input().split()
a, b = map(int,[a,b])
result = ""
if s == ">":
    result = "Right" if a > b else "Wrong"
elif s == "<":
    result = "Right" if a < b else "Wrong"
else:
    result = "Right" if a == b else "Wrong"
print(result)
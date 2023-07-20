x = float(input())

if x.is_integer():
    print("int", int(x))
else:
    print("float", int(x), x - int(x))
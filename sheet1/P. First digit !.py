x = input()

last_digit = x[0:1]
last_digit = int(last_digit)
if last_digit % 2 == 0:
    print("EVEN")
else:
    print("ODD")
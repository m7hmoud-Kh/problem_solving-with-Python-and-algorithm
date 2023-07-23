def fact(number):
    if number <= 1:
        return 1
    return number * fact(number-1)

n = int(input())
for i in range(n):
    x  = int(input())
    print(fact(x))



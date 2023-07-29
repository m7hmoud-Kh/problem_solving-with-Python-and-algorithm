n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    max_number,min_number = [max(a,b),min(a,b)]
    summation = 0
    for i in range(min_number+1,max_number):
        if i % 2 != 0:
            summation += i
    print(summation)
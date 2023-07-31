n, a, b = map(int,input().split())

all_summation = 0
for i in range(1,n+1):
    summation_of_digit = 0
    num = i
    while num > 0:
        digit = num % 10
        summation_of_digit += digit
        num=int(num/10)
    if int(summation_of_digit) >= a and int(summation_of_digit) <= b:
        all_summation += i
print(all_summation)



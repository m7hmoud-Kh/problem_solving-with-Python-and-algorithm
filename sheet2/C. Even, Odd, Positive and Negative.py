x = int(input())
Odd = 0
Even = 0
Positive = 0
Negative = 0
j = list(map(int, input().split()))
for i in j[:x]:
    if i % 2 == 0:
        Even += 1
    else:
        Odd += 1
    if i > 0:
        Positive += 1
    elif i < 0:
        Negative += 1
print("Even:",Even)
print("Odd:",Odd)
print("Positive:",Positive)
print('Negative:',Negative)

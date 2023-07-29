a, b = map(int, input().split())

while a > 0 and b > 0 :
    max_number,min_number = [max(a,b),min(a,b)]
    summation = 0
    for i in range(min_number,max_number+1):
        summation += i
        print(i,end=" ")
    print("sum =", summation,sep="")
    a, b = map(int, input().split())


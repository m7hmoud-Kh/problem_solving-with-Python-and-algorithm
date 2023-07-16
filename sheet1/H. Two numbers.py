import math
a, b = map(int,input().split())
print("floor {} / {} =".format(a,b), math.floor(a/b))
print("ceil {} / {} =".format(a,b), math.ceil(a/b))
print("round {} / {} =".format(a,b), int((a/b)+0.5))


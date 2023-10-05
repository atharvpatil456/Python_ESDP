import math

def ssum(x, n):
    return math.log(1 + x)

def expsum(x, n):
    return math.exp(x)

x = 2
n = 5
res = ssum(x, n)
print("Sum of the series :",res)

res = expsum(x, n)
print("Sum of exp series :",res)
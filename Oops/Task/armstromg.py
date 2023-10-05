def armstrong(num):
    numstr = str(num)
    numdigits = len(numstr)
    armsum = sum(int(digit)**numdigits for digit in numstr)
    return armsum == num

for i in range(1, 9001):
    if armstrong(i):
        print(i)
